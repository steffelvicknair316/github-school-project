import random
def generate_random_code(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join([charset[random.randrange(0, len(charset))] for i in range(length)])