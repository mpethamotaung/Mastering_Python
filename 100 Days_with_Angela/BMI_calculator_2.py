#Welcome to the BMI calculator

height = float(input("What is your height\n"))
weight = int(input("what is your weight\n"))

bmi = weight/(height*height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <25:
    print(f"Your BMI is {bmi}, your have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
