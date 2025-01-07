# input() = A function that prompts the user to enter data.
#           Returns the entered data as a string.

input("What is your name: ")

# we can also assign it in variable

age = input("What is your age: ")

# Since input() functions returns the entered data into string we can't add or use any operation on it.
# This where we use the typecasting.

age = int(age)
age = age + 1
print("Happy Birthday!")
print(f"You're age is {age} years old.")

# Here is the other way to declare it.

num1 = int(input("Please enter Num 1: "))
num2 = int(input("Please enter Num 2: "))

print(f"The sum of num1 and num2 is equal to {num1 + num2}")
