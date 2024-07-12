#Using aqcuired list knowledge to build a treasure map

line1 = ['','','']
line2 = ['','','']
line3 = ['','','']
map = [line1, line2,line3]
print("Hiding your treasure! X marks the spot")
position = input("Add letter A,B,C followed by 1,2,3 (example: A1)") #Where do you want to put the treasure?
#Grab first letter and make it lowercase
letter = position[0].lower() 
#List that presents the three possible letters
abc = ['a','b','c'] 
#create a variable letter_index assign it to abc our list .index(letter)
letter_index = abc.index(letter) 
#Take input that comes through input variable position
number_index = int(position[1]) - 1 
#Bring up nested list and include created indeces to insert 'x'
map[number_index][letter_index] = "X"


print(f'{line1}\n{line2}\n{line3}')