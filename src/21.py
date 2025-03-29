import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
print(calculate_distance(0, 0, 3, 4)) # Output: 5.0
