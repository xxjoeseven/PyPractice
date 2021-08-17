import random

#Ascii Art

rock = '''
     _________
____/    ______)
         ______)
_____    ______)  ROCK
     \\______)
'''
scissor = '''
    __________
___/    ______)
       |______
___    _______) SCISSOR
   \\   _____)
    \\___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______) PAPER
         _______)
---.__________)
'''

ascii_art = [rock, paper, scissor]

user_input = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
print(ascii_art[user_input])

machine_input = random.randint(0,2)
print("Machine throws:\n")
print(ascii_art[machine_input])

if user_input >= 3 or user_input < 0:
  print("Oei, 0 for rock, 1 for Paper, 2 for Scissor! You lose!")
elif user_input == 0 and machine_input == 2:
  print("You win!")
elif machine_input == 0 and user_input == 2:
  print("You lose~")
elif machine_input > user_input:
  print("You lose")
elif user_input > machine_input:
  print("You win!")
elif user_input == machine_input:
  print("It's a draw!")
