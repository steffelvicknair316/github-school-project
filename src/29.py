def calculate_area(radius):
    import math
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
