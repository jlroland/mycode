#!/usr/bin/env python3
"""TLG NDE Cohort April 2022 | Trivia Game from Data File"""

from trivia import trivia
import random

# GOALS
# using a for loop, return each question one at a time
# print out the question
# use a for loop to print out the "answers"
# prompt the user to make a choice

counter = 1

for x in trivia["results"]:
    print(f"{counter}. {x['question']}")
    counter += 1
    
    all_answers= x["incorrect_answers"]
    
    all_answers.append(x['correct_answer'])
    
    random.shuffle(all_answers)

    letters= ["A.","B.","C.","D."]
    answer_ind = all_answers.index(x['correct_answer'])
    correct_answer = letters[answer_ind]

    for letter,answer in zip(letters,all_answers):
        print(letter, answer)


    answer= input("\n>")

    if answer.upper() == correct_answer.rstrip("."):
        print("Correct!")
    else:
        print("Wrong!")

    print()
