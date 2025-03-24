def calculate_sum(x: int, y: int) -> int:
    """
    Calculate the sum of two integers.
    
    Args:
        x (int): The first integer.
        y (int): The second integer.
        
    Returns:
        int: The sum of the two integers.
    """
    return x + y

def main():
    number1 = 5
    number2 = 3
    result = calculate_sum(number1, number2)
    print("The sum is:", result)

if __name__ == "__main__":
    main()
