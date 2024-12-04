# test_user_data.py
import unittest
from user_data import validate_user_data

class TestUserDataValidation(unittest.TestCase):

    def test_valid_data(self):
        # Geçerli kullanıcı verileri
        users = [
            {'name': 'Alice', 'age': 30,'email': 'alice@example.com'},
            {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'}
        ]
        invalid_users = validate_user_data(users)
        self.assertEqual(invalid_users, [])  # Hiçbir geçersiz kullanıcı olmamalı

    def test_invalid_age(self):
        # Geçersiz yaş
        users = [
            {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
            {'name': 'Bob', 'age': 120, 'email': 'bob@example.com'}
        ]
        invalid_users = validate_user_data(users)
        self.assertIn("Invalid age for Bob", invalid_users)  # Bob'un yaşı geçersiz

    def test_invalid_email(self):
        # Geçersiz e-posta
        users = [
            {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
            {'name': 'Bob', 'age': 25, 'email': 'bob@example'}  # Geçersiz e-posta
        ]
        invalid_users = validate_user_data(users)
        self.assertIn("Invalid email for Bob", invalid_users)  # Bob'un e-posta adresi geçersiz

    def test_invalid_age_and_email(self):
        # Hem yaş hem de e-posta geçersiz
        users = [
            {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
            {'name': 'Bob', 'age': 120, 'email': 'bob@example'}  # Bob'un hem yaşı hem de e-posta adresi geçersiz
        ]
        invalid_users = validate_user_data(users)
        self.assertIn("Invalid age for Bob", invalid_users)
        self.assertIn("Invalid email for Bob", invalid_users)

if __name__ == "__main__":
    unittest.main()
