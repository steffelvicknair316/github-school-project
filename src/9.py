import random

def get_random_code():
    """Generates a random 8-digit alphanumeric code"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    password = ''
    for i in range(8):
        password += random.choice(letters) + random.choice(numbers)
    return password