import pyfiglet
from colorama import Fore

from config import ASCII_ART_GENERATOR
from shared.color_processor import colors, fonts, FontProcessor, ColorProcessor
from shared.file_processors import FileProcessor


class AsciiArtGeneratorService:

    def __init__(self):
        self.__file_processor = FileProcessor()

    @staticmethod
    def __get_text(text, font, color_position, width) -> str:
        fig = pyfiglet.Figlet(font)
        fig.width = width
        formatted_text = fig.renderText(text)
        return getattr(Fore, colors[color_position]) + formatted_text

    def display_text(self):
        while True:
            try:
                initial_text = str(input("Enter text containing all ASCII characters "
                                         "in order to display: "))
                if not initial_text.isascii():
                    print("Text must contain only ASCII characters")
                    continue
                FontProcessor.display_fonts()
                font_position = int(input("Enter position of font you would like to use: "))
                ColorProcessor.display_colors()
                color_position = int(input("Enter position of color you would like to use: "))
                width = int(input("Enter width of text you "
                                  "would like to display: "))
                modified_text = self.__get_text(initial_text, fonts[font_position],
                                                color_position, width)
                print(modified_text)
                self.__file_processor.write_into_file(ASCII_ART_GENERATOR, modified_text)

                while True:
                    if input(
                            "Would you like to continue? Enter 'Y' or 'y' if you do, or "
                            "anything else if you don't. Your response is ").lower() == "y":
                        continue
                    break
            except ValueError:
                print("Cannot be parsed into an int value")
            except KeyError:
                print("You have entered a wrong value for the key of fonts or color")
            except pyfiglet.CharNotPrinted as e:
                print(str(e))
