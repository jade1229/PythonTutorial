# Get the area of a circle
# Formula is A = pi * r2

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of a circle is equal to {round(area, 2)}")