import string
import secrets

class PasswordGenerator:
    def __init__(self, length: int):
        self.length = length

    @staticmethod
    def _generate_candidate_password(length: int) -> str:
        printable = string.printable[:-6]
        password = [secrets.choice(printable) for _ in range(length)]
        return ''.join(password)

    def generate_password(self) -> str:
        password = self._generate_candidate_password(self.length)

        while not self._is_valid_password(password):
            password = self._generate_candidate_password(self.length)

        return password

    def _is_valid_password(self, password: str) -> bool:
        return bool(
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c in string.punctuation for c in password)
            and sum(c.isdigit() for c in password)
        )
# Generate 16 character password

print(PasswordGenerator(16).generate_password())
