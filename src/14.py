import random

def get_random_code():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "{", "[", "}", "]", "|", ";", ":", "<", ",", ">"]
    code = ""
    for i in range(10):
        code += random.choice(numbers)
    for i in range(5):
        code += random.choice(letters)
    for i in range(5):
        code += random.choice(special_characters)
    return code