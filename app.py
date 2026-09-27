import os
import time

from dt_utility import (
    clear_screen,
    format_seconds,
    display_divider,
    get_formated_now,
    display_main_divider,
    display_error_message,
    display_title_message,
)

from typing import Final
from shutil import copytree
from shutil import ignore_patterns

VERSION: Final[str] = "1.6.0"

SOURCE_PATH: Final[str] = "D:/Source_Codes"
DESTINATION_PATH: Final[str] = f"E:/SOURCE_CODES_WITH_GIT"

IGNORE_PATTERNS: Final = ignore_patterns(
    # ********************
    # Some Files (Maybe Important!)
    # ********************
    # "*.pdf".strip().lower(),
    # "*.doc".strip().lower(),
    # "*.docx".strip().lower(),
    # ********************
    # Some Files
    # ********************
    "*.log".strip().lower(),
    "*.pkl".strip().lower(),
    "*.tmp".strip().lower(),
    "*.temp".strip().lower(),
    "*.weights".strip().lower(),
    "*.egg-info".strip().lower(),
    # ********************
    # Some Binary Files
    # ********************
    "*.db".strip().lower(),
    "*.dat".strip().lower(),
    "*.dll".strip().lower(),
    "*.exe".strip().lower(),
    "*.msi".strip().lower(),
    "*.sqlite3".strip().lower(),
    # ********************
    # Some Compressed Files
    # ********************
    "*.7z".strip().lower(),
    "*.jar".strip().lower(),
    "*.rar".strip().lower(),
    "*.tar".strip().lower(),
    "*.zip".strip().lower(),
    # ********************
    # Some Image Files
    # ********************
    "*.bmp".strip().lower(),
    "*.gif".strip().lower(),
    "*.svg".strip().lower(),
    # "*.png".strip().lower(),  # Check this later
    "*.jpg".strip().lower(),  # Check this later
    "*.jpeg".strip().lower(),  # Check this later
    "*.tiff".strip().lower(),
    # ********************
    # Some AI Files
    # ********************
    "*.ie".strip().lower(),
    "*.ot".strip().lower(),
    "*.pt".strip().lower(),
    "*.h5".strip().lower(),
    "*.bak".strip().lower(),
    "*.bin".strip().lower(),
    "*.eot".strip().lower(),
    "*.fst".strip().lower(),
    "*.int".strip().lower(),
    "*.map".strip().lower(),
    "*.mdl".strip().lower(),
    "*.pkl".strip().lower(),
    "*.sym".strip().lower(),
    "*.suo".strip().lower(),
    "*.whl".strip().lower(),
    "*.avif".strip().lower(),
    "*.dubm".strip().lower(),
    "*.nemo".strip().lower(),
    "*.onnx".strip().lower(),
    "*.pack".strip().lower(),
    "*.scss".strip().lower(),
    "*.task".strip().lower(),
    "*.user".strip().lower(),
    "*.webp".strip().lower(),
    "*.carpa".strip().lower(),
    "*.data*".strip().lower(),
    "*.sample".strip().lower(),
    "*.tflite".strip().lower(),
    "*.incomplete".strip().lower(),
    "*.safetensors".strip().lower(),
    # ********************
    # Some Video Files
    # ********************
    "*.avi".strip().lower(),
    "*.mkv".strip().lower(),
    "*.mp4".strip().lower(),
    "*.wmv".strip().lower(),
    # ********************
    # Some Audio Files
    # ********************
    "*.mp3".strip().lower(),  # Check this later
    "*.ogg".strip().lower(),
    "*.wav".strip().lower(),  # Check this later
    # ********************
    # Some Special Folders
    # ********************
    ".vs".strip().lower(),
    "venv".strip().lower(),
    ".venv".strip().lower(),
    ".models".strip().lower(),
    ".venv.3.9".strip().lower(),
    ".venv.3.10".strip().lower(),
    ".venv.3.11".strip().lower(),
    ".venv.3.12".strip().lower(),
    ".venv.3.13".strip().lower(),
    ".venv.3.14".strip().lower(),
    ".venv.3.15".strip().lower(),
    ".venv.3.16".strip().lower(),
    ".pytest_cache".strip().lower(),
    # ********************
    # Some Folders
    # ********************
    "bin".strip().lower(),
    "obj".strip().lower(),
    "tmp".strip().lower(),
    "dist".strip().lower(),
    "temp".strip().lower(),
    "build".strip().lower(),
    "wheels".strip().lower(),
    "install".strip().lower(),
    "packages".strip().lower(),
    "__pycache__".strip().lower(),
    # GIT Files and Folders
    # "logs".strip().lower(),  # Check this later
    # ".git".strip().lower(),  # Check this later
)


def main() -> None:
    """Main function"""

    clear_screen()
    display_main_divider()
    message: str = f"Dariush Tasdighi - Copy Files - Version {VERSION}"
    display_title_message(message=message)

    destination_path: str = f"{DESTINATION_PATH}_{get_formated_now()}"
    os.makedirs(name=destination_path, exist_ok=True)

    display_divider()
    message: str = f"Copying files from [{SOURCE_PATH}] to [{destination_path}]..."
    print(message, end=" ", flush=True)

    start_time: float = time.perf_counter()

    copytree(
        src=SOURCE_PATH,
        dirs_exist_ok=True,
        dst=destination_path,
        ignore=IGNORE_PATTERNS,
    )

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time
    formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

    print()
    display_divider()
    print(f"Elapsed Time: {formatted_elapsed_time}")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as exception:
        display_divider()
        display_error_message(message=str(exception))

    finally:
        display_main_divider()
        print()
