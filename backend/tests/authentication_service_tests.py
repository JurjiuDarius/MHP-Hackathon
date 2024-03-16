import unittest
from unittest.mock import MagicMock, patch
from service.authenticatin_service import login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.mock_user_query = MagicMock()
        self.mock_user = MagicMock()

    def test_login_success(self):
        data = {
            "email": "test@example.com",
            "password": "password",
            "role": "employee"
        }

        self.mock_user.password = "hashed_password"
        self.mock_user.serialize.return_value = {"id": 1, "email": "test@example.com", "role": "employee"}

        with patch('service.authenticatin_service.login') as mock_user_query, \
             patch('service.authenticatin_service.create_token') as mock_create_token:
            mock_user_query.filter_by.return_value.first.return_value = self.mock_user
            mock_create_token.return_value = "mocked_token"

            response, status_code = login(data)

            self.assertEqual(status_code, 200)
            self.assertEqual(response['token'], "mocked_token")
            self.assertEqual(response['user'], {"id": 1, "email": "test@example.com", "role": "employee"})

    def test_login_invalid_role(self):
        data = {
            "email": "test@example.com",
            "password": "password",
            "role": "invalid_role"
        }

        response, status_code = login(data)

        self.assertEqual(status_code, 400)
        self.assertEqual(response['message'], "Invalid role!")

    def test_login_incorrect_password(self):
        data = {
            "email": "test@example.com",
            "password": "incorrect_password",
            "role": "employee"
        }

        self.mock_user.password = "hashed_password"
        self.mock_user.serialize.return_value = {"id": 1, "email": "test@example.com", "role": "employee"}

        with patch('service.authenticatin_service.login') as mock_user_query:
            mock_user_query.filter_by.return_value.first.return_value = self.mock_user

            response, status_code = login(data)

            self.assertEqual(status_code, 401)
            self.assertEqual(response['message'], "Incorrect password!")


if __name__ == '__main__':
    unittest.main()
