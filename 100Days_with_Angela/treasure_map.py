#Using aqcuired list knowledge to build a treasure map

line1 = ['','','']
line2 = ['','','']
line3 = ['','','']
map = [line1, line2,line3]
print("Hiding your treasure! X marks the spot")
position = input("Add letter A,B,C followed by 1,2,3 (exampl: A1)") #Where do you want to put the treasure?

letter = position[0].lower() #Grab first letter and make it lowercase
abc = ['a','b','c'] #List that presents the three possible letters


print(f'{line1}\n{line2}\n{line3}')