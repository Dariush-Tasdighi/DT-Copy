# **************************************************
# import os
# import sys
# import time

# from typing import Final

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_error_message,
#     display_title_message,
# )

# WIDTH: Final[int] = 100
# VERSION: Final[str] = "1.1.0"

# # SOURCE_PATH: Final[str] = "./temp"
# # SOURCE_PATH: Final[str] = "D:/Temp"
# # SOURCE_PATH: Final[str] = "./.venv.3.14"
# SOURCE_PATH: Final[str] = "C:/Users/dariu"
# # SOURCE_PATH: Final[str] = "D:/Source_Codes"


# def check_directory_exists(path: str) -> None:
#     """Check directory exists"""

#     message: str

#     if not os.path.exists(path=path):
#         message = f"Directory '{path}' Not Found"
#         raise Exception(message)

#     if not os.path.isdir(s=path):
#         message = f"Directory '{path}' Not Found"
#         raise Exception(message)


# def main() -> None:
#     """Main Function"""

#     clear_screen()
#     display_main_divider(count=WIDTH)
#     message: str = f"Detect All File Formats - Version {VERSION}"
#     display_title_message(message=message)

#     check_directory_exists(path=SOURCE_PATH)

#     start_time: float = time.perf_counter()

#     file_count: int = 0
#     file_extensions: dict = {}

#     for _, _, files in os.walk(top=SOURCE_PATH, topdown=True):
#         for file in files:
#             file_count += 1
#             file_extension: str = os.path.splitext(file)[1].lower().strip()

#             if file_extension == "":
#                 file_extension = "[NO_EXTENSION]"

#             if file_extension not in file_extensions:
#                 file_extensions[file_extension] = 1
#             else:
#                 file_extensions[file_extension] += 1

#     file_extensions = dict(
#         sorted(
#             file_extensions.items(),
#             reverse=True,
#             key=lambda item: item[1],
#         )
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     display_divider(count=WIDTH)
#     print(f"File Count     : {file_count:,}")
#     display_divider(count=WIDTH)
#     print(f"Extension Count: {len(file_extensions):,}")
#     display_divider(count=WIDTH)
#     print(f"Elapsed Time   : {formatted_elapsed_time}")
#     display_divider(count=WIDTH)

#     for index, file_extension in enumerate(file_extensions, start=1):
#         file_extension_count: int = int(file_extensions[file_extension])
#         message: str = f"{index:>6,}|{file_extension:<84}|{file_extension_count:>8,}"
#         # print(len(message))  # For Debugging!
#         # sys.exit()  # For Debugging!
#         print(message)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         pass

#     except Exception as exception:
#         display_divider(count=WIDTH)
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider(count=WIDTH)
#         print()
# **************************************************


# **************************************************
# import os
# import sys
# import time

# from typing import Final

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_error_message,
#     display_title_message,
# )

# WIDTH: Final[int] = 100
# VERSION: Final[str] = "1.1.0"

# # SOURCE_PATH: Final[str] = "."
# # SOURCE_PATH: Final[str] = "./temp"
# # SOURCE_PATH: Final[str] = "D:/Temp"
# # SOURCE_PATH: Final[str] = "./.venv.3.14"
# # SOURCE_PATH: Final[str] = "C:/Users/dariu"
# SOURCE_PATH: Final[str] = "D:/Source_Codes"

# # NEW
# # IGNORE_DIRS: Final[set] = {".temp"}
# IGNORE_DIRS: Final[set] = {
#     "tmp".strip().lower(),
#     "temp".strip().lower(),
#     "models".strip().lower(),
#     "wheels".strip().lower(),
#     "install".strip().lower(),
#     "__pycache__".strip().lower(),
#     "packages".strip().lower(),
#     "node_modules".strip().lower(),
#     #
#     ".vs".strip().lower(),
#     "bin".strip().lower(),
#     "obj".strip().lower(),
#     "dist".strip().lower(),
#     "build".strip().lower(),
#     #
#     "venv".strip().lower(),
#     ".venv".strip().lower(),
#     ".venv.3.9".strip().lower(),
#     ".venv.3.10".strip().lower(),
#     ".venv.3.11".strip().lower(),
#     ".venv.3.12".strip().lower(),
#     ".venv.3.13".strip().lower(),
#     ".venv.3.14".strip().lower(),
#     ".venv.3.15".strip().lower(),
#     #
#     ".git".strip().lower(),
# }


# def check_directory_exists(path: str) -> None:
#     """Check directory exists"""

#     message: str

#     if not os.path.exists(path=path):
#         message = f"Directory '{path}' Not Found"
#         raise Exception(message)

#     if not os.path.isdir(s=path):
#         message = f"Directory '{path}' Not Found"
#         raise Exception(message)


# def main() -> None:
#     """Main Function"""

#     clear_screen()
#     display_main_divider(count=WIDTH)
#     message: str = f"Detect All File Formats - Version {VERSION}"
#     display_title_message(message=message)

#     check_directory_exists(path=SOURCE_PATH)

#     start_time: float = time.perf_counter()

#     file_count: int = 0
#     file_extensions: dict = {}

#     # NEW
#     # for _, _, files in os.walk(top=SOURCE_PATH, topdown=True):
#     for _, dirs, files in os.walk(top=SOURCE_PATH, topdown=True):
#         # NEW
#         dirs[:] = [dir for dir in dirs if dir.strip().lower() not in IGNORE_DIRS]

#         for file in files:
#             file_count += 1

#             # NEW
#             # file_extension: str = os.path.splitext(file)[1].lower().strip()
#             # if file_extension == "":
#             #     file_extension = "[NO_EXTENSION]"

#             file_extension: str = (
#                 os.path.splitext(file)[1].lower().strip() or "[NO_EXTENSION]"
#             )

#             if file_extension not in file_extensions:
#                 file_extensions[file_extension] = 1
#             else:
#                 file_extensions[file_extension] += 1

#     file_extensions = dict(
#         sorted(
#             file_extensions.items(),
#             reverse=True,
#             key=lambda item: item[1],
#         )
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     display_divider(count=WIDTH)

#     for index, file_extension in enumerate(file_extensions, start=1):
#         file_extension_count: int = int(file_extensions[file_extension])
#         message: str = f"{index:>6,}|{file_extension:<84}|{file_extension_count:>8,}"
#         # print(len(message))  # For Debugging!
#         # sys.exit()  # For Debugging!
#         print(message)

#     display_divider(count=WIDTH)
#     print(f"Path                : {SOURCE_PATH}")
#     display_divider(count=WIDTH)
#     print(f"File Extension Count: {len(file_extensions):,}")
#     display_divider(count=WIDTH)
#     print(f"File Count          : {file_count:,}")
#     display_divider(count=WIDTH)
#     print(f"Elapsed Time        : {formatted_elapsed_time}")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         pass

#     except Exception as exception:
#         display_divider(count=WIDTH)
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider(count=WIDTH)
#         print()
# **************************************************


# **************************************************
# Just Cleaned!
# **************************************************
import os
import time

from typing import Final

from dt_utility import (
    clear_screen,
    format_seconds,
    display_divider,
    display_main_divider,
    display_error_message,
    display_title_message,
)

WIDTH: Final[int] = 100
VERSION: Final[str] = "1.1.0"
SOURCE_PATH: Final[str] = "D:/Source_Codes"

IGNORE_DIRS: Final[set] = {
    "tmp".strip().lower(),
    "temp".strip().lower(),
    "models".strip().lower(),
    "wheels".strip().lower(),
    "install".strip().lower(),
    "__pycache__".strip().lower(),
    "packages".strip().lower(),
    "node_modules".strip().lower(),
    #
    ".vs".strip().lower(),
    "bin".strip().lower(),
    "obj".strip().lower(),
    "dist".strip().lower(),
    "build".strip().lower(),
    #
    "venv".strip().lower(),
    ".venv".strip().lower(),
    ".venv.3.9".strip().lower(),
    ".venv.3.10".strip().lower(),
    ".venv.3.11".strip().lower(),
    ".venv.3.12".strip().lower(),
    ".venv.3.13".strip().lower(),
    ".venv.3.14".strip().lower(),
    ".venv.3.15".strip().lower(),
    #
    ".git".strip().lower(),
}


def check_directory_exists(path: str) -> None:
    """Check directory exists"""

    message: str

    if not os.path.exists(path=path):
        message = f"Directory '{path}' Not Found"
        raise Exception(message)

    if not os.path.isdir(s=path):
        message = f"Directory '{path}' Not Found"
        raise Exception(message)


def main() -> None:
    """Main Function"""

    clear_screen()
    display_main_divider(count=WIDTH)
    message: str = f"Detect All File Formats - Version {VERSION}"
    display_title_message(message=message)

    check_directory_exists(path=SOURCE_PATH)

    start_time: float = time.perf_counter()

    file_count: int = 0
    file_extensions: dict = {}

    for _, dirs, files in os.walk(top=SOURCE_PATH, topdown=True):
        dirs[:] = [dir for dir in dirs if dir.strip().lower() not in IGNORE_DIRS]

        for file in files:
            file_count += 1

            file_extension: str = (
                os.path.splitext(file)[1].lower().strip() or "[NO_EXTENSION]"
            )

            if file_extension not in file_extensions:
                file_extensions[file_extension] = 1
            else:
                file_extensions[file_extension] += 1

    file_extensions = dict(
        sorted(
            file_extensions.items(),
            reverse=True,
            key=lambda item: item[1],
        )
    )

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time
    formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

    display_divider(count=WIDTH)

    for index, file_extension in enumerate(file_extensions, start=1):
        file_extension_count: int = int(file_extensions[file_extension])
        message: str = f"{index:>6,}|{file_extension:<84}|{file_extension_count:>8,}"
        print(message)

    display_divider(count=WIDTH)
    print(f"Path                : {SOURCE_PATH}")
    display_divider(count=WIDTH)
    print(f"File Extension Count: {len(file_extensions):,}")
    display_divider(count=WIDTH)
    print(f"File Count          : {file_count:,}")
    display_divider(count=WIDTH)
    print(f"Elapsed Time        : {formatted_elapsed_time}")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as exception:
        display_divider(count=WIDTH)
        display_error_message(message=str(exception))

    finally:
        display_main_divider(count=WIDTH)
        print()
# **************************************************
