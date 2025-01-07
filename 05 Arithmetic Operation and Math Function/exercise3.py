# Calculate the hypotenuse of a triangle
# The formula is c = sqrt(a^2 + b^2)

import math

a = float(input("Enter the side a of the triangle: "))
b = float(input("Enter the side b of the triangle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of a triangle is: {round(c, 2)}")

