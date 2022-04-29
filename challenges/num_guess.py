#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num= random.randint(1,100)
    rounds= 0
    
    while rounds < 5:
        guess= input("Guess a number between 1 and 100\n>")
        
        # COOL CODE ALERT: what is the purpose of the next fourlines?
        if guess.isdigit():
            guess= int(guess)
        else:
            # add the following line to limit total guesses to 5, to include non-numeric ones
            # rounds += 1
            continue

        if guess > num:
            print("Too high!")
            rounds += 1

        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")
            break

if __name__ == "__main__":
    main()
