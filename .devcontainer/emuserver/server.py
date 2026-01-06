#!/usr/bin/env python3
# emu_server.py — minimal static server + ROM discovery/streaming (stdlib only)
# - Static site from --web-root (default: ./web)
# - JSON list at /_roms (all *.gba under --rom-root, default: /workspaces)
# - Safe streaming at /rom/<relative-path>
# - Clean CLI flags; robust error handling (500 on unexpected errors)

import argparse
import http.server
import socketserver
import os
import json
import urllib.parse
import sys
from contextlib import suppress

def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Minimal EmulatorJS helper server")
    p.add_argument("--host", default="0.0.0.0", help="Host/IP to bind (default: 0.0.0.0)")
    p.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    p.add_argument("--web-root", default=os.path.abspath("./web"),
                   help="Directory to serve static files from (default: ./web)")
    p.add_argument("--rom-root", default="/workspaces",
                   help="Directory to recursively search/serve .gba files (default: /workspaces)")
    return p.parse_args(argv)

def is_within(path: str, root: str) -> bool:
    try:
        rp, rr = os.path.realpath(path), os.path.realpath(root)
        return rp == rr or rp.startswith(rr + os.sep)
    except Exception:
        return False

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, web_root=None, rom_root=None, **kwargs):
        self._web_root = web_root
        self._rom_root = rom_root
        super().__init__(*args, directory=self._web_root, **kwargs)

    # ----------- utilities -----------
    def _write_bytes(self, status: int, ctype: str, data: bytes, cache_no_store: bool = True):
        """Small helper to avoid duplicated header boilerplate."""
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        if cache_no_store:
            self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_500(self, message: str = "Internal Server Error"):
        # Standard error body (plain text)
        self._write_bytes(500, "text/plain; charset=utf-8", message.encode("utf-8"))

    def _send_404(self, message: str = "Not Found"):
        self._write_bytes(404, "text/plain; charset=utf-8", message.encode("utf-8"))

    # ----------- routing -----------
    def do_GET(self):
        try:
            parsed = urllib.parse.urlsplit(self.path)
            path = parsed.path

            if path == "/_roms":
                return self._handle_roms()

            if path.startswith("/rom/"):
                rel = path[len("/rom/"):]
                return self._handle_rom_stream(rel)

            # Everything else: let SimpleHTTPRequestHandler serve from web_root
            return super().do_GET()

        except BrokenPipeError:
            # Client disconnected mid-response; ignore quietly
            pass
        except Exception as e:
            # Unexpected failure -> 500
            with suppress(Exception):
                self._send_500("Internal Server Error")
            # Optional: uncomment to log exceptions to stderr
            # print(f"500 on {self.path}: {e}", file=sys.stderr)

    # ----------- handlers -----------
    def _handle_roms(self):
        """Return JSON array of every .gba under rom_root (recursive, relative paths)."""
        try:
            roms = []
            rr = self._rom_root
            root_len = len(rr.rstrip(os.sep)) + 1
            for dirpath, dirnames, filenames in os.walk(rr):
                # Skip noisy dot-dirs to keep it snappy
                dirnames[:] = [d for d in dirnames if not d.startswith(".")]
                for fn in filenames:
                    if fn.lower().endswith(".gba"):
                        full = os.path.join(dirpath, fn)
                        if is_within(full, rr):
                            rel = full[root_len:].replace(os.sep, "/")
                            roms.append(rel)
            roms.sort(key=lambda s: s.lower())

            body = json.dumps(roms).encode("utf-8")
            self._write_bytes(200, "application/json; charset=utf-8", body)
        except Exception:
            self._send_500("Failed to enumerate ROMs")

    def _handle_rom_stream(self, rel_path: str):
        """Stream a .gba from rom_root safely."""
        try:
            rel_path = rel_path.lstrip("/")
            full = os.path.normpath(os.path.join(self._rom_root, rel_path))
            if not (full.lower().endswith(".gba") and is_within(full, self._rom_root) and os.path.isfile(full)):
                return self._send_404("ROM not found")

            # Use application/octet-stream; browsers won't try to sniff.
            fs = os.stat(full)
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", str(fs.st_size))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            with open(full, "rb") as f:
                while True:
                    chunk = f.read(64 * 1024)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
        except Exception:
            self._send_500("Failed to stream ROM")

    # Optional: quiet logs. Comment out to see access logs.
    # def log_message(self, fmt, *args):
    #     return super().log_message(fmt, *args)

def main(argv=None):
    args = parse_args(argv)

    web_root = os.path.abspath(args.web_root)
    rom_root = os.path.abspath(args.rom_root)

    if not os.path.isdir(web_root):
        print(f"ERROR: web root does not exist: {web_root}", file=sys.stderr)
        return 2
    if not os.path.isdir(rom_root):
        print(f"ERROR: rom root does not exist: {rom_root}", file=sys.stderr)
        return 2

    HandlerCls = lambda *a, **kw: Handler(*a, web_root=web_root, rom_root=rom_root, **kw)

    with socketserver.TCPServer((args.host, args.port), HandlerCls) as httpd:
        print(f"Serving static from: {web_root}")
        print(f"ROM listing/streaming from: {rom_root}")
        print(f"Open: http://{args.host}:{args.port}/   (/_roms lists ROMs, /rom/<path> streams)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
