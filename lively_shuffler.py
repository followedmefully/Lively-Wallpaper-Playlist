import os
import subprocess
import random
import time
import json

config_path = "config.json" # relative to the script

# Seed with current time (or os.urandom internally)
random.seed(time.time())

def get_random_wallpaper(folder):
    folders = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, f))
    ]

    if not folders:
        return None

    return random.choice(folders)

with open(config_path, "r") as f:
    config = json.load(f)

lively_path = config.get("lively_path")
delay = config.get("delay_seconds", 1800)
wallpaper_folder = config.get("wallpaper_folder")
monitors = config.get("monitors", [1])


while True:
    for monitor in monitors:
        wallpaper = get_random_wallpaper(wallpaper_folder)

        if wallpaper:
            subprocess.run([
                lively_path,
                "setwp",
                "--file", wallpaper,
                "--monitor", str(monitor)
            ],
            creationflags=subprocess.CREATE_NO_WINDOW,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )

    time.sleep(delay)