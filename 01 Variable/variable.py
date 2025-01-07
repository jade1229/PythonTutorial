# Variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it contains.

# string = a series of text (this could be in "" or '').
first_name = "Jade Mark"
food = "burger"
email = "gimpaojade4@gmail.com"

# fstring = a string with f or F before the opening quotation mark or triple
#           quotation mark. Inside this string, you can write a Python expression
#           between { and } characters that can be referred to variable or literal values.
# f or F  = means format.

print(f"Hello {first_name}")
print(f"I like {food}")
print(f"My email is {email}\n")

# integers = an integer is a data type used to represent whole numbers.
#            it is typically displayed as-is—just the number itself—without quotes or special characters.

age = 25
quantity = 4

print(f"I am {age} years old.")
print(f"i have a total of {quantity} pieces of mango.\n")

# floats = a floats (short for "floating-point number") is data type used to represent
#          that have a decimal point or can be fractional form.
#          it is commonly used for measurements, calculation with precision, and values that are not whole numbers.

price = 19.23
gpa = 2.3
distance = 10.213

print(f"The price of coke is {price} pesos.")
print(f"My GPA when I was a college is {gpa}.")
print(f"I ran about {distance} kilometers.\n")

# boolean = is a data type that represents one of the two values: True or False.
#           it is often used to make decision or control the flow of a program with conditions.

is_student = False
for_sale = True

print(f"Are you a student: {is_student}")

if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")