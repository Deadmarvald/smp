import pyfiglet
from colorama import Fore

fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))

colors = {
    1: 'WHITE',
    2: 'RED',
    3: 'BLUE',
    4: 'YELLOW',
    5: 'GREEN',
    6: 'MAGENTA'
}

def display_fonts():
    print("Доступні шрифти:")
    for i, font in fonts.items():
        print(f"{i}. {font}")

def display_colors():
    print("Доступні кольори:")
    for i, color in colors.items():
        print(f"{i}. {color}")

def get_text(text, font, color_position, width):
    fig = pyfiglet.Figlet(font)
    fig.width = width
    formatted_text = fig.renderText(text)
    return getattr(Fore, colors[color_position]) + formatted_text

def write_in_file(file_path, text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def read_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()