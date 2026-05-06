import os
import sys
import shutil
import subprocess
import platform

MAIN_APP = "malware.py"
UI_APP = "decript-window.py"

BUILD_DIR = "build"


def clean():
    print("[+] Cleaning old builds...")

    for folder in [BUILD_DIR, "temp_build", "temp_spec"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    for f in os.listdir():
        if f.endswith(".spec"):
            os.remove(f)

    print("[+] Clean done.\n")


def run_pyinstaller(script, name, extra_args=None):
    if extra_args is None:
        extra_args = []

    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--distpath", os.path.join(BUILD_DIR, current_os),
        "--workpath", "temp_build",
        "--specpath", "temp_spec",
        "--name", name,
        script,
        *extra_args
    ])


def build_linux():
    print("[🐧] Building Linux executables...")

    run_pyinstaller(MAIN_APP, "malware")
    run_pyinstaller(UI_APP, "decript-window")

    print("[✔] Linux build done.\n")


def build_windows():
    print("[🪟] Building Windows executables...")

    run_pyinstaller(MAIN_APP, "malware.exe")
    run_pyinstaller(UI_APP, "decript-window.exe")

    print("[✔] Windows build done.\n")


if __name__ == "__main__":
    clean()

    current_os = platform.system().lower()

    os.makedirs(os.path.join(BUILD_DIR, "windows"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "linux"), exist_ok=True)

    # ⚠️ importante: build só funciona nativamente bem por OS
    if current_os == "windows":
        build_windows()

    elif current_os == "linux":
        build_linux()

    else:
        print("Unsupported OS")
        sys.exit(1)

    # cleanup
    for folder in ["temp_build", "temp_spec"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    print("[🎯] Build complete!")
    print(f"[📦] Output: ./{BUILD_DIR}/")