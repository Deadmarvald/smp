from ascii_art_generator import *

def save_to_file(destination_path, content) -> None:
    with open(destination_path, "w") as output_file:
        output_file.write(content)


def load_from_file(source_path) -> str:
    with open(source_path, "r") as input_file:
        return input_file.read()


def main():
    try:
        user_input_text = str(input("Input text to convert to ASCII art: "))
        AbstractDataHandler.show_color_options()
        chosen_color_index = int(input("Choose a color index: "))
        desired_width = int(input("Set the width for ASCII art: "))
        alphabet_file_path = "ascii_alphabet.txt"
        ascii_processor = TextFileHandler(alphabet_file_path)
        ascii_art = ascii_processor.fetch(user_input_text, chosen_color_index, desired_width)
        print(ascii_art)
        save_to_file("ascii_output.txt", ascii_art)
    except KeyError:
        print("Error: Incorrect color index or missing characters in the ASCII file.")
    except ValueError as ve:
        print(ve)
    except FileNotFoundError:
        print("Error: ASCII character file not found. Please verify the path.")

if __name__ == "__main__":
    main()