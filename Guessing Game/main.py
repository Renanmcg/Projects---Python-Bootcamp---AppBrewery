#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import Art as a
from random import randint
lives = 0
print(a.logo)
print("Welcome to the guessing game!")
print(" You have to find what number i'm thinking on.")
difficulty = input('What difficulty do you want: Hard? Easy?')
if difficulty in 'Hard':
  lives = 5
else:
  lives = 10
computer = randint(0, 100)
answer = 999
while answer != computer:  
  answer = int(input('Choose a number between 0 and 100: '))
  if answer == computer:
    print("Great you got it!")
  elif answer > computer:
    lives -= 1
    print(f"Too High! You have {lives} lives left.")
    if lives == 0:
      print(f"You lose! The number was {computer}")
      break
  else:
    lives -= 1
    print(f'Too low! You have {lives} lives left.')
    if lives == 0:
      print(f"You lose! The number was {computer}")
      break
