import math

# Get user input
a = float(input("Enter your Hypotenuse (a): "))
b = float(input("Enter your Opposite side (b): "))
c = float(input("Enter your Adjacent side (c): "))


# Calculate trigonometric ratios
sine = b / a        # sin(θ) = opposite / hypotenuse
cosine = c / a      # cos(θ) = adjacent / hypotenuse
tangent = b / c     # tan(θ) = opposite / adjacent

# Display results
print("✨ Trigonometric Values ✨")
print("Sine  (opposite/hypotenuse):", sine)
print("Cosine(adjacent/hypotenuse):", cosine)
print("Tangent(opposite/adjacent):", tangent)
