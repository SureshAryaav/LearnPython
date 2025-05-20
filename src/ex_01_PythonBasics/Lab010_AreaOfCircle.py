# Import math library to use pi
import math

# Ask the user to enter the radius
radius_input = input("Enter the radius of the circle: ")

# Validate and calculate
if radius_input.replace('.', '', 1).isdigit():
	radius = float(radius_input)
	area = math.pi * radius ** 2
	
	print(f"The area of the circle with radius {radius} is {area:.2f}")
else:
	print("Please enter a valid number for radius.")