# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print(f"Item bought: {item}")
print(f"Item price: {price} pesos")
print(f"Quantity of item: {quantity}")
print(f"Total amount to be paid: {total}")