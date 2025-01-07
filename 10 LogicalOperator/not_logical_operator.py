# logical operators = evaluate multiple conditions (or, and, not)
#                     not = inverts the condition (not False, not True)

# Create a program that identify whether it is sunny or not.

temp = float(input("Enter the current temperature (Degree Celsius): "))

# A loop for invalid input

while True:
    is_sunny_input = input("Enter if it's sunny or not (True or False): ").strip().lower()
    if is_sunny_input == "true":
        is_sunny = True
        break
    elif is_sunny_input == "false":
        is_sunny = False
        break
    else:
        print("Invalid input, please enter 'True' or 'False'")

# Check conditions

if temp >= 28 and is_sunny:
    print("It is HOT outside!")
    print("It is SUNNY!")
elif temp <= 0 and is_sunny:
    print("It is COLD outside!")
    print("It is SUNNY!")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside!")
    print("It is SUNNY!")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside!")
    print("It is CLOUDY!")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside!")
    print("It is CLOUDY!")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside!")
    print("It is CLOUDY!")
else:
    print("It is not SUNNY!")