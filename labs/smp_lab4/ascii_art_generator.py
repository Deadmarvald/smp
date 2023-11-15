import os
import re
from abc import ABC, abstractmethod
import colorama
from colorama import Fore
from functools import reduce

colorama.init(autoreset=True)
color_palette = {index: color for index, color in enumerate(sorted(Fore.__dict__.keys()))}


class AbstractDataHandler(ABC):

    def __init__(self, path_to_file):
        if not path_to_file:
            raise ValueError("Path to file cannot be empty")
        self._file_path = path_to_file

    @abstractmethod
    def _read_and_process_data(self) -> None:
        pass

    @abstractmethod
    def fetch(self, text, color_index, line_width) -> str:
        pass

    def _load_file_content(self) -> str:
        with open(self._file_path, 'r') as file:
            return file.read()

    @staticmethod
    def show_color_options() -> None:
        for index, color_name in color_palette.items():
            print(f"{index}. {color_name}")


class TextFileHandler(AbstractDataHandler):
    _meta_info = {}
    _content = {}

    def __init__(self, path_to_file):
        if not path_to_file.endswith(".txt") or not os.path.exists(path_to_file):
            raise ValueError("File must be a .txt file and exist")
        super().__init__(path_to_file)
        self._read_and_process_data()

    def _read_and_process_data(self) -> None:
        file_content = self._load_file_content().split("\n")
        data_section_found = False
        symbol_representation = ""
        current_symbol = None

        for line in file_content:
            if data_section_found:
                if re.match("^@symbol::.$", line):
                    if current_symbol:
                        self._content[current_symbol] = symbol_representation
                    current_symbol = line[-1]
                    symbol_representation = ""
                    row_length = 0
                    line_counter = 1
                elif re.match("^\\^.+\\$$", line):
                    if line_counter == 1:
                        row_length = len(line)
                    if len(line) != row_length:
                        raise ValueError("Inconsistent row length for symbol representation")
                    symbol_representation += line[1:-1] + ("\n" if line_counter < self._meta_info["height"] else "")
                    line_counter += 1
                else:
                    raise ValueError("Incorrect format in data section")
            elif line == "@data":
                if "height" not in self._meta_info:
                    raise ValueError("Meta information 'height' is missing")
                data_section_found = True
            elif not data_section_found:
                if re.match("^\\w+::\\d+$", line):
                    key, value = line.split("::")
                    self._meta_info[key] = int(value)
                else:
                    raise ValueError("Invalid meta data format")

    def fetch(self, text, color_index, max_width) -> str:
        symbol_data = {}
        needed_symbols = {}
        line_properties = {}
        current_line = 0
        current_line_width = 0

        for index, char in enumerate(text):
            symbol_lines = self._content[char].split("\n")
            if current_line_width + len(symbol_lines[0]) > max_width:
                if len(symbol_lines[0]) > max_width:
                    raise ValueError("Text width too small")
                current_line += 1
                current_line_width = 0
            current_line_width += len(symbol_lines[0])
            line_properties[current_line] = line_properties.get(current_line, 0) + 1
            needed_symbols[index] = "\n".join(symbol_lines)

        symbol_index = 0
        for line in line_properties:
            for _ in range(line_properties[line]):
                lines = needed_symbols[symbol_index].split("\n")
                symbol_index += 1
                for row_index, row in enumerate(lines):
                    line_key = row_index + line * self._meta_info["height"]
                    symbol_data[line_key] = symbol_data.get(line_key, "") + row

        colored_output = Fore.__getattribute__(color_palette[color_index])
        return colored_output + "\n".join(symbol_data.values())