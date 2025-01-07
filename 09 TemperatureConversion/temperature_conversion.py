# Temperature conversion exercise:

unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter temperature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "Fahrenheit"
    print(f"You're temperature in Fahrenheit is: {round(temp, 2)} {unit}")
elif unit == "F":
    temp = (temp - 32) * (5 / 9)
    unit = "Celsius"
    print(f"You're temperature in Celsius is: {round(temp, 2)} {unit}")
else:
    print("Invalid unit of measure, please try again!")

