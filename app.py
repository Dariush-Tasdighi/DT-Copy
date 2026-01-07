import os
import time
from shutil import copytree
from datetime import datetime
from shutil import ignore_patterns

VERSION: str = "1.5.0"
SOURCE_PATH: str = "D:\\Source_Codes"
DESTINATION_PATH: str = f"E:\\SOURCE_CODES_WITH_GIT"

IGNORE = ignore_patterns(
    # Some Files
    "*.log".lower(),
    "*.pkl".lower(),
    "*.tmp".lower(),
    "*.weights".lower(),
    "*.egg-info".lower(),
    # Some Binary Files
    "*.db".lower(),
    "*.dat".lower(),
    "*.dll".lower(),
    "*.exe".lower(),
    "*.msi".lower(),
    "*.sqlite3".lower(),
    # Some Compressed Files
    "*.7z".lower(),
    "*.rar".lower(),
    "*.tar".lower(),
    "*.zip".lower(),
    # Some Image Files
    "*.bmp".lower(),
    # "*.png".lower(),  # Check this later
    "*.jpg".lower(),
    "*.jpeg".lower(),
    "*.tiff".lower(),
    # Some AI Files
    "*.h5".lower(),
    "*.onnx".lower(),
    # Some Video Files
    "*.avi".lower(),
    "*.mp4".lower(),
    "*.mkv".lower(),
    "*.wmv".lower(),
    # Some Audio Files
    "*.wav".lower(),
    "*.ogg".lower(),
    # "*.mp3".lower(),  # Check this later
    # Some Special Folders
    ".vs".lower(),
    ".venv".lower(),
    ".models".lower(),
    ".pytest_cache".lower(),
    # Some Folders
    "bin".lower(),
    "obj".lower(),
    "tmp".lower(),
    "dist".lower(),
    "temp".lower(),
    "build".lower(),
    "wheels".lower(),
    "install".lower(),
    "packages".lower(),
    "__pycache__".lower(),
    # GIT Files and Folders
    # "logs".lower(),  # Check this later
    # ".git".lower(),  # Check this later
)


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    current_time = datetime.now()
    current_time_str = current_time.strftime(format="%Y_%m_%d_%H_%M_%S")
    destination_path: str = f"{DESTINATION_PATH}_{current_time_str}"

    if not os.path.exists(path=destination_path):
        os.makedirs(name=destination_path)

    print("Please wait...")
    print(f"Copying files from {SOURCE_PATH} to {destination_path}...")

    start_time: float = time.time()

    copytree(
        ignore=IGNORE,
        src=SOURCE_PATH,
        dirs_exist_ok=True,
        dst=destination_path,
    )

    response_time: float = time.time() - start_time

    print(f"Copy process completed in {response_time:.2f} seconds.")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"\n[-] {error}!")

    print()
