# constant and math function
# but will need to import math module for it's full functionality or be avail to use it.

import math

# to use math module we have first to declare the "math" then follows by "." and the function name.

print("The value of pi is: ", math.pi)

# e = means exponential constant
print("The value of e is: ", math.e)

# math.sqrt = calculate the square root of a number
x = 81
result = math.sqrt(x)
print(f"The square root of {x} is equal to {result}")

# math.ceil = round the floating number up.
y = 12.3
a = math.ceil(y)
print(f"The ceiling number of {y} is equal to {a}")

# math.floor = round the floating number down.
b = math.floor(y)
print(f"The floor value of {y} is equal to {b}")