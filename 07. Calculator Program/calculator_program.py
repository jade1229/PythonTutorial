# python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

if operator == "+":
    print(f"The sum of num 1 and num 2 is equal to: {num1 + num2}")
elif operator == "-":
    print(f"The difference of num 1 and num 2 is equal to: {num1 - num2}")
elif operator == "*":
    print(f"The product of num 1 and num 2 is equal to: {num1 * num2}")
elif operator == "/":
    print(f"The quotient of num 1 and num 2 is equal to: {num1 / num2}")
else:
    print("Please try again, invalid operators!")

