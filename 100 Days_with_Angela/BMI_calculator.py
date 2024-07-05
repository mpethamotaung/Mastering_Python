#BMI calculator

#Variables definition
print("Let's calculate your BMI")
height = input("What is your height\n")
weight = input("What is your weight\n")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float **2

print("Your BMI is: ", + bmi)


