# Calculate the circumference of a circle
# Formula is C = 2*pi*r

import math

radius = float(input("Enter the radius: "))

circumference = 2 * math.pi * radius

# You can round the results by using round() function.
print(f"The circumference of a circle is: {round(circumference, 2)}")