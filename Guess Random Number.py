import  random
import re 
import sys


def guess(x):
    random_number= random.randint(1,x)
    guess= 0
    while guess != random_number:
        guess= int(input(f"guess a number between1 and {x}:"))
        
        if guess < random_number:
            print("too low")

        elif guess > random_number:
            print('too high')
    print(f"Well done you guessed the number {random_number}")
  
guess(15)