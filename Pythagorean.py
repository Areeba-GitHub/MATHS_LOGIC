# How To Create a Pythagorean Theroem Program Using Python.

import math

# Get user input
b = float(input("Enter the length of perpendicular side: "))
c = float(input("Enter the length of base side: "))

# Calculate the square of the sides
b_square = b**2
c_square = c**2

a = math.sqrt(b_square + c_square)  # Calculate hypotenuse using Pythagorean theorem

# Values
print("✨ Pythagorean Theorem Values ✨")
print("Length of Hypotenuse (a):", a)
print("Length of Perpendicular side (b):", b)
print("Length of Base side (c):", c)

