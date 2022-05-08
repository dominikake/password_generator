import unittest
import string

class TestPassword(unittest.TestCase):
    def test_password(self):
        password = password_generator()
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        numbers = string.digits
        punctuation = string.punctuation
        self.assertTrue(any(char in lower_case for char in password))
        self.assertTrue(any(char in upper_case for char in password))
        self.assertTrue(any(char in numbers for char in password))
        self.assertTrue(any(char in punctuation for char in password))

if __name__ == '__main__':
    unittest.main()