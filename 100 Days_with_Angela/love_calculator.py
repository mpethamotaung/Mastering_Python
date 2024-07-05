print("The love calculator is calculating your score...")
name1 = input("What is your name (boy)")
name2 = input("What is your name (girl)")

combined_names = name1 + name2 #Combining names into 1 digit
lower_names = combined_names.lower() # Convert names to lowercase

t = lower_names.count("t") #We use count to check the letter occurence in combined names
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e #Add upp all occurences

l = lower_names.count("l") #We use count to check the letter occurence in combined names
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e #Add up all occurences

#Final score is first + second digit
score = int(str(first_digit) + str(second_digit)) #Convert digits to strings to combine them and covert to int

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>=40) and (score <=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
