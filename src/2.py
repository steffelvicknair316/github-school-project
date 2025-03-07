import random

def get_random_integer(n):
    return random.randint(0, n)

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

def get_random_boolean():
    return random.randint(0, 1) == 1
