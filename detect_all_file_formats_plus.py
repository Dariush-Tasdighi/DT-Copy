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

    for root, _, files in os.walk(top=SOURCE_PATH, topdown=True):
        for file in files:
            file_count += 1
            file_extension: str = os.path.splitext(file)[1].lower()

            if file_extension == "":
                file_extension = "[NO_EXTENSION]"

            file_length: int = os.path.getsize(os.path.join(root, file))

            if file_extension not in file_extensions:
                file_extensions[file_extension] = [1, file_length]
            else:
                file_extensions[file_extension][0] += 1
                file_extensions[file_extension][1] += file_length

    response_time: float = time.time() - start_time

    file_extensions = dict(
        sorted(
            file_extensions.items(),
            key=lambda item: item[1][1],
            reverse=True,
        )
    )

    separator_length: int = 67

    print("=" * separator_length)
    print(f"File Count: {file_count:,.0f}")
    print("-" * separator_length)
    print(f"Extension Count: {len(file_extensions):,.0f}")
    print("-" * separator_length)
    print(f"Process completed in {response_time:.2f} seconds.")
    print("-" * separator_length)

    sum: int = 0

    for index, file_extension in enumerate(file_extensions):
        sum += file_extensions[file_extension][1]

        new_index = f"{(index + 1):,.0f}"
        new_index = new_index.rjust(5)

        new_file_extension = file_extension.ljust(28)

        file_extension_count = f"{file_extensions[file_extension][0]:,.0f}"
        file_extension_count = file_extension_count.rjust(8)

        total_file_length = f"{file_extensions[file_extension][1]:,.0f}"
        total_file_length = total_file_length.rjust(16)

        print(
            f"[{new_index}]: {new_file_extension} - {file_extension_count} - {total_file_length}"
        )

    if sum > 1024 * 1024 * 1024:
        print("-" * separator_length)
        print(f"Total File Size: {sum / (1024 * 1024 * 1024):,.0f} GB")

    if sum > 1024 * 1024:
        print("-" * separator_length)
        print(f"Total File Size: {sum / (1024 * 1024):,.0f} MB")

    if sum > 1024:
        print("-" * separator_length)
        print(f"Total File Size: {sum / 1024:,.0f} KB")

    print("-" * separator_length)
    print(f"Total File Size: {sum:,.0f} B")

    print("=" * separator_length)
    print()


if __name__ == "__main__":
    main()
