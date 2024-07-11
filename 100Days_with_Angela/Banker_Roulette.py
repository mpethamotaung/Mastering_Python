#Banker Roulette, pick random name and print
import random

#Create a list variable and list items
names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
#Ger the total number of items in list.
num_items = len(names_string) #Calculate how many items in list
#Generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items-1)
#Choose and print a random name.
print(names_string[random_choice])
