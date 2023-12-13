from config import logger
from ui.menu.lab2.calculator_menu import CalculatorMenu
from ui.menu.lab3.ascii_art_generator_menu import AsciiArtGeneratorMenu
from ui.menu.lab4.own_ascii_art_generator import OwnAsciiArtGeneratorMenu
from ui.menu.lab5.figures import FigureMenu
from ui.menu.lab7.user_menu import UserMenu
from ui.menu.lab8.diagrams_menu import DiagramMenu


class Runner:

    def __init__(self):
        self.__calculator = CalculatorMenu()
        self.__ascii_art_generator = AsciiArtGeneratorMenu()
        self.__own_ascii_art_generator = OwnAsciiArtGeneratorMenu()
        self.__figure = FigureMenu()
        self.__user_menu = UserMenu()
        self.__diagram_menu = DiagramMenu()

    def run(self):
        print("Welcome to the main menu!")
        while True:
            try:
                print("Please, choose the lab you would like to run")
                print("1. Lab 2")
                print("2. Lab 3")
                print("3. Lab 4")
                print("4. Lab 5")
                print("5. Lab 7")
                print("6. Lab 8")
                print("7. Exit")
                choice = int(input("Your choice is "))
                if choice == 1:
                    self.__calculator.run()
                elif choice == 2:
                    self.__ascii_art_generator.run()
                elif choice == 3:
                    self.__own_ascii_art_generator.run()
                elif choice == 4:
                    self.__figure.run()
                elif choice == 5:
                    self.__user_menu.run()
                elif choice == 6:
                    self.__diagram_menu.run()
                elif choice == 7:
                    break
                else:
                    logger.error("The number is not defined in the list")
                    print("Wrong input! Please, try again")
            except ValueError:
                logger.error("The input is not a number")
                print("Wrong input! Please, try again")


if __name__ == '__main__':
    runner = Runner()
    runner.run()
