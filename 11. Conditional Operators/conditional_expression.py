# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on condition
#                          X if condition else Y

num = int(input("Enter a number: "))

# This line of code will determine if the input number is positive or negative
# Using conditional expression.

# print("Positive" if num > 0 else "Negative")

# Determine whether the input number is EVEN or ODD number
# Using conditional expression

print("EVEN" if num % 2 == 0 else "ODD")

# Here's another way to write this conditional expression

result = "POSITIVE" if num > 0 else "NEGATIVE"
print(result)