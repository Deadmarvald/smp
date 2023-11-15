def write_into_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
