#Ticket Calculator with nested if /else statement

height = int(input("What is your height"))
age = int(input("What is your age"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
else:
    print("You cannot ride the roller coaster")