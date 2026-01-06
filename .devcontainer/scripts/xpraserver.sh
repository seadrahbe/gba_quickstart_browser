#!/usr/bin/env bash

# Start LibreSprite in xpra
# Disable MIT-SHM for Xvfb (causes issues under qemu on amd64)
# TODO: Investigate whether it's worth probing for MIT-SHM failure before falling back
xpra start :100  \
     --bind-tcp=0.0.0.0:14500 \
     --html=on \
     --daemon=no \
     --exit-with-children \
     --opengl=off \
     --system-tray=off \
     --notifications=off \
     --printing=off \
     --pulseaudio=off \
     --webcam=off \
     --mdns=off \
     --xvfb="Xvfb +extension Composite -nolisten tcp -noreset -extension MIT-SHM" \
     --start-child="/tools/libresprite/AppRun"