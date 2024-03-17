import hashlib
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from service.authenticatin_service import login


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.mock_user_query = MagicMock()
        self.mock_user = MagicMock()

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.db = SQLAlchemy(self.app)
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

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

        with patch('service.authenticatin_service.User.query', return_value=self.mock_user_query):
            self.mock_user_query.filter_by.return_value.first.return_value = self.mock_user

            response, status_code = login(data)

            self.assertEqual(status_code, 401)
            self.assertEqual(response['message'], "Incorrect password!")


if __name__ == '__main__':
    unittest.main()
