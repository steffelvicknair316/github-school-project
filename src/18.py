def square_root(num):
    if num < 0:
        return "Error: Negative number does not have a real square root."
    
    guess = num / 2.0
    while True:
        next_guess = (guess + num / guess) / 2.0
        if abs(guess * guess - num) < 1e-6:
            return next_guess
        elif guess ** 2 > num:
            return next_guess
        else:
            guess = next_guess

# Example usage:
result = square_root(9)
print(f"The square root of {9} is approximately {result}")
