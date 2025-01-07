# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be True

# Create an if statement, if the user input the temperature which is above 35 degree
# or lower than 0 degree or raining the outdoor event will be cancelled.

temp = float(input("Enter the current temperature (Degree Celsius): "))
is_raining_input = input("Enter if it's raining or not (True or False): ").strip().lower()

# converts string to boolean.
# The reason why we need to convert string to boolean instead of using typecast it's because
# any non-empty value of bool() is always "True" and if it's empty it is "False".

if is_raining_input == "true":
    is_raining = True
elif is_raining_input == "false":
    is_raining = False
else:
    print("Invalid input, please input True or False")
    exit()

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is scheduled!")

