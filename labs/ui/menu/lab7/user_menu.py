import json

from config import TWITTER_ACC_INFO_JSON, TWITTER_ACC_INFO_CSV, TWITTER_ACC_INFO_TXT
from service.lab7.user_service import DisplayInTableService, UserService
from shared import json_processor
from shared.color_processor import ColorProcessor
from shared.file_processors import FileProcessor


class UserMenu:

    @staticmethod
    def run():
        history: list = []
        successful_result: bool = False
        jsons: list = []

        while True:
            print("Choose an option:")
            print("1. Display data of a Twitter personal profile")
            print("2. Save data")
            print("3. Show history")
            print("0. Exit")

            option = input("Your choice: ")
            match option:
                case "1":
                    jsons = []
                    twitter_username = input("Enter Twitter username: ")
                    try:
                        jsons = UserService.get_personal_profile(twitter_username)
                        print("Choose an option:")
                        print("1. Display data in a flattened way")
                        print("2. Display data in JSON format")
                        print("3. Display data in a table")
                        while True:
                            option = input("Your choice: ")
                            match option:
                                case "1":
                                    ColorProcessor.display_colors()
                                    color_position = int(input("Enter a color position: "))
                                    json_processor.display_flattened_json(jsons, color_position)
                                    break
                                case "2":
                                    print(json.dumps(jsons, indent=4))
                                    break
                                case "3":
                                    print(DisplayInTableService.display_personal_profile(
                                        json.dumps(jsons, indent=4)))
                                    break
                                case _:
                                    print("Invalid option. Enter again!")
                        history.append(
                            f"Data of a Twitter personal profile for username "
                            f"{twitter_username}:\n{json.dumps(jsons, indent=4)}")
                        successful_result = True
                    except ValueError as e:
                        print(e)
                        successful_result = False

                case "2":
                    if successful_result:
                        try:
                            FileProcessor.write_into_json(TWITTER_ACC_INFO_JSON, jsons)
                            FileProcessor.write_into_csv(TWITTER_ACC_INFO_CSV, jsons)
                            FileProcessor.write_into_txt(TWITTER_ACC_INFO_TXT, jsons)
                            print("Data saved in JSON, CSV, and TXT formats.")
                        except Exception as e:
                            print(f"Error saving data: {e}")
                    else:
                        print("No data to save!")

                case "3":
                    if len(history) == 0:
                        print("No history!")
                    else:
                        for counter, item in enumerate(history):
                            print(f"{counter + 1}: {item}")

                case "0":
                    break

                case _:
                    print("Invalid option. Enter again!")
