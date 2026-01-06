let enableDebug = true;
let enableThreads = false;
let browserMode;

const urlParams = new URLSearchParams(window.location.search);

if (parseInt(urlParams.get("threads")) === 1 || urlParams.get("threads") === "true") {
    if (window.SharedArrayBuffer) {
        enableThreads = true;
        console.log("Threads are enabled");
    } else {
        console.warn("Threads are disabled as SharedArrayBuffer is not available.");
        console.log("Threads are disabled");
    }
} else {
    console.log("Threads are disabled");
}

if (urlParams.get("browserMode")) {
    browserMode = urlParams.get("browserMode");
}

// If a rom query parameter is present, load immediately; otherwise list from /_roms.
if (urlParams.get("rom")) {
    const romPath = urlParams.get("rom");
    console.log(`Loading ROM from server: /rom/${romPath}`);
    run(romPath);
} else {
    listRoms();
}

// Fetch list from /_roms and render
async function listRoms() {
    const container = document.getElementById("rom-list");
    try {
        const r = await fetch("/_roms", { cache: "no-store" });
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        const arr = await r.json();
        renderList(Array.isArray(arr) ? arr : []);
    } catch (e) {
        console.error("Could not list ROMs:", e);
        container.textContent = "No ROMs found or listing failed.";
    }

    function renderList(files) {
        const c = document.getElementById("rom-list");
        c.innerHTML = "";
        if (!files.length) {
            c.textContent = "No ROMs found. Change to your game directory and compile your game using 'make'. Check to make sure there's no compilation errors!";
            return;
        }
        files.forEach(name => {
            const btn = document.createElement("button");
            btn.className = "rom-btn";
            btn.textContent = name;
            btn.onclick = () => run(name);
            c.appendChild(btn);
        });
    }
}

// Run a selected ROM via the server's /rom/<path>
async function run(relativePath) {
    const url = `/rom/${encodeURI(relativePath)}`;
    const fileName = relativePath.split("/").pop();
    const parts = (fileName || "").split(".");

    // Build display container
    const div = document.createElement("div");
    const sub = document.createElement("div");
    const script = document.createElement("script");

    sub.id = "game";
    div.id = "display";

    const top = document.getElementById("top");
    if (top) top.remove();
    const box = document.getElementById("box");
    if (box) box.remove();

    div.appendChild(sub);
    document.body.appendChild(div);

    // Configure EmulatorJS (GBA only)
    window.EJS_player = "#game";
    window.EJS_gameName = parts.slice(0, -1).join(".") || fileName || relativePath;
    window.EJS_biosUrl = "";
    window.EJS_gameUrl = url;
    window.EJS_core = "gba";
    window.EJS_pathtodata = "https://cdn.emulatorjs.org/latest/data/";
    window.EJS_startOnLoaded = true;
    window.EJS_DEBUG_XX = enableDebug;
    window.EJS_disableDatabases = true;
    window.EJS_threads = enableThreads;
    if (browserMode) {
        window.EJS_browserMode = browserMode;
    }

    // Load runtime from CDN
    script.src = "https://cdn.emulatorjs.org/latest/data/loader.js";
    document.body.appendChild(script);
}