import string
import secrets


def generate_password() -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c in string.punctuation for c in password)
            and sum(c.isdigit() for c in password)):
            
            print(password)
        break

generate_password()
