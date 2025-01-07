# python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (Kgs or Lbs): ")

if unit == "Kgs":
    weight = weight * 2.205
    unit = "lbs"
    print(f"You're weight into pounds is {round(weight, 2)} {unit}")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "kgs"
    print(f"You're weight into kilogram is {round(weight, 2)} {unit}")
else:
    print("Invalid unit of measure, please try again!")

