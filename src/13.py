def get_random_python_code():
    import random
    from string import ascii_letters, digits

    num_lines = random.randint(10, 20)
    lines = []
    for i in range(num_lines):
        line = ''.join(random.choice(ascii_letters + digits) for _ in range(random.randint(10, 50)))
        lines.append(line)

    return '\n'.join(lines)
