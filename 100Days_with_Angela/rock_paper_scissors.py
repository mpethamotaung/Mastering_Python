#Rock,Paper, Scissors game against the computer

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
choice =   ['Rock', 'Paper', 'Scissors']
computer_choice = random.randint(choice[1]-1) 