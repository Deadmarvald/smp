import json
import requests
from prettytable import PrettyTable
import regex
import config
from config import logger

class UserService:

    @staticmethod
    def get_personal_profile(twitter_username: str):
        if not twitter_username or not isinstance(twitter_username, str):
            raise ValueError("Username must be a non-empty string!")

        query_params = {"username": twitter_username}
        headers = {
            "X-RapidAPI-Key": config.X_RAPID_API_KEY,
            "X-RapidAPI-Host": config.X_RAPID_API_HOST
        }
        response = requests.get(config.GET_PERSONAL_PROFILE, headers=headers, params=query_params)
        if response.status_code != 200:
            message = response.json().get('message', 'Unknown error occurred!')
            logger.error("Error: %s", message)
            raise ValueError(f"Error occurred! {message}")

        return response.json()

class DisplayInTableService:

    @staticmethod
    def display_personal_profile(json_data: str):
        data = json.loads(json_data)

        table = PrettyTable()
        table.field_names = ["Attribute", "Value"]

        allowed_keys = {
            "user_id", "username", "name", "follower_count", "following_count",
            "favourites_count", "is_private", "is_verified", "location",
            "profile_pic_url", "profile_banner_url", "description", "external_url",
            "number_of_tweets", "bot"
        }

        for key, value in data.items():
            if key in allowed_keys:
                table.add_row([key, value])

        return table.get_string()