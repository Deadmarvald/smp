import json
import unittest
from unittest.mock import patch
from service.lab7.user_service import UserService, DisplayInTableService
from shared.file_processors import FileProcessor

class TestUserService(unittest.TestCase):

    @patch('service.lab7.user_service.requests.get')
    def test_get_personal_profile_valid(self, mock_get):
        # Припустимо, що API повертає успішну відповідь для валідного користувача
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "username": "test_user", "user_id": "123", "follower_count": 100
        }

        response = UserService.get_personal_profile("test_user")
        self.assertIn("username", response)
        self.assertIn("test_user", response["username"])

    @patch('service.lab7.user_service.requests.get')
    def test_get_personal_profile_invalid(self, mock_get):
        # Припустимо, що API повертає помилку для невалідного запиту
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": "User not found"}

        with self.assertRaises(ValueError):
            UserService.get_personal_profile("invalid_user")

class TestDisplayInTableService(unittest.TestCase):

    def test_display_personal_profile(self):
        json_data = json.dumps({"username": "test_user", "user_id": "123"})
        table_string = DisplayInTableService.display_personal_profile(json_data)
        self.assertIn("test_user", table_string)

class TestFileProcessor(unittest.TestCase):

    def test_write_into_json(self):
        test_data = [{"key": "value"}]
        FileProcessor.write_into_json("test.json", test_data)
        with open("test.json", "r") as file:
            data = json.load(file)
        self.assertEqual(test_data, data)

if __name__ == '__main__':
    unittest.main()
