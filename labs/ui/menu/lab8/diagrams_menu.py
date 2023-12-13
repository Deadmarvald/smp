import sys
from config import USERS_DATA
from service.lab8.diagrams_service import DiagramServiceImpl


class DiagramMenu:

    def run(self):
        service = DiagramServiceImpl(USERS_DATA)

        while True:
            print(
                "1. Display difference in thousands histogram\n"
                "2. Display sex pie chart\n"
                "3. Display state bar chart\n"
                "4. Display combined diagram\n"
                "0. Exit\n"
            )

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.display_diagram(service.create_difference_in_thousands_histogram)
                case "2":
                    self.display_diagram(service.create_sex_pie_chart)
                case "3":
                    self.display_diagram(service.create_state_bar_chart)
                case "4":
                    self.display_diagram(service.create_combined_diagram)
                case "0":
                    sys.exit(0)
                case _:
                    print("Invalid choice. Enter again!")

    @staticmethod
    def display_diagram(diagram_function):
        has_to_be_downloaded = input(
            "Do you want to download the diagram? Enter 'y' or "
            "anything else not to download: ") == "y"

        diagram_function(has_to_be_downloaded)
