def is_even(n):
    """
    Checks if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

# Example usage:
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is not an even number.")
