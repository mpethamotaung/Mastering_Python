#Ticket Calculator with nested if statements with midlife crisis

height = int(input("What is your height"))
age = int(input("What is your age"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill = 5
        print("Children tickets are $5")
    elif age <= 18:
        bill = 7
        print("Yout tickets are $7")
    elif age >=45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo? Y or N.")
    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("You cannot ride the roller coaster")