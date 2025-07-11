import math

# Function to calculate the base area of a pyramid
def calculate_base_area(shape):
    shape = shape.lower()
    
    if shape == 'square':
        side = float(input("Enter the side length of the square: "))
        return side ** 2
    
    elif shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return length * width

    elif shape == 'triangle':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return 0.5 * base * height
        
    else:
        print("ValueError ❌ Unsupported shape for base area calculation.")

# Ask user for shape
shape = input("What's the shape of your pyramid's base? (square, rectangle, triangle): ")

# Get base area
base_area = calculate_base_area(shape)

# Get height of pyramid
height = float(input("Enter the height of the pyramid: "))

# Calculate volume
def calculate_volume(base_area, height):
    return (1/3) * base_area * height

volume = calculate_volume(base_area, height)

# Displaying results
print("\n✨ Pyramid Volume Calculation ✨")
print(f"Base Area: {base_area}")
print(f"Height: {height}")
print(f"Volume: {volume}")







