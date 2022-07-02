import unittest
import string
from main import generate_password

class TestPassword(unittest.TestCase):
    def test_password(self) -> str:
        
        password = generate_password()
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        numbers = string.digits
        punctuation = string.punctuation

        self.assertTrue(any(char in lower_case for char in password))
        self.assertTrue(any(char in upper_case for char in password))
        self.assertTrue(any(char in numbers for char in password))
        self.assertTrue(any(char in punctuation for char in password))
        self.assertEqual(len(password), 8)

if __name__ == '__main__':
    unittest.main()