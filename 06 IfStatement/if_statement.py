# if = Do some code only if some condition is True
#      Else do something else.

age = int(input("Enter your age: "))

if age <= 12:
    print("You are a child!")
elif 13 <= age <= 19:
    print("You're a teenager!")
elif 20 <= age <= 60:
    print("You are an adult!")
else:
    print("You're seasoned!")