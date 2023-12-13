import colorama
import pyfiglet
from colorama import Fore

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))
fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))


class ColorProcessor:

    @staticmethod
    def display_colors() -> None:
        for i in colors:
            print(str(i) + ". " + colors[i])


class FontProcessor:

    @staticmethod
    def display_fonts() -> None:
        for i in fonts:
            print(str(i) + ". " + fonts[i])
