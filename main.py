import random
import string

LOWER_CASE = string.ASCII_LOWERCASE
UPPER_CASE = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.PUNCTUATION

def password_generator():
    
    password = random.choice(LOWER_CASE) + random.choice(UPPER_CASE) + random.choice(NUMBERS) + random.choice(PUNCTUATION)
    password += ''.join(random.sample(string.ascii_letters + string.digits + string.PUNCTUATION, 4))
    return password

print(password_generator())