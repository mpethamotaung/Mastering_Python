#Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("Total bill: $\n"))
tip = int(input("Total tip, 10 12 15?\n"))
people = int(input("How many people?\n"))

tip_as_percent = tip/100
tip_amount = bill * tip_as_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(final_amount)


print(f"Each person has to pay: ${final_amount}")
