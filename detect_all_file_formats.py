import os
import time

SOURCE_PATH: str = "D:\\Source_Codes"


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    file_count: int = 0
    file_extensions: dict = {}

    start_time: float = time.time()

    for _, _, files in os.walk(top=SOURCE_PATH, topdown=True):
        for file in files:
            file_count += 1
            file_extension: str = os.path.splitext(file)[1].lower()

            if file_extension == "":
                file_extension = "[NO_EXTENSION]"

            if file_extension not in file_extensions:
                file_extensions[file_extension] = 1
            else:
                file_extensions[file_extension] += 1

    response_time: float = time.time() - start_time

    file_extensions = dict(
        sorted(
            file_extensions.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )

    separator_length: int = 50

    print("=" * separator_length)
    print(f"File Count: {file_count:,.0f}")
    print("-" * separator_length)
    print(f"Extension Count: {len(file_extensions):,.0f}")
    print("-" * separator_length)
    print(f"Process completed in {response_time:.2f} seconds.")
    print("-" * separator_length)

    for index, file_extension in enumerate(file_extensions):
        new_index = f"{(index + 1):,.0f}"
        new_index = new_index.rjust(5)

        new_file_extension = file_extension.ljust(30)

        file_extension_count = f"{file_extensions[file_extension]:,.0f}"
        file_extension_count = file_extension_count.rjust(8)

        print(f"[{new_index}]: {new_file_extension} - {file_extension_count}")

    print("=" * separator_length)
    print()


if __name__ == "__main__":
    main()
