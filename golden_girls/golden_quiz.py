#!/usr/bin/env python3

#initialize baseline score for tabulation
#lowest score is Rose, then Blanche, then Dorothy, then Sophia with highest score
score = 0

response1 = input("How many sarcastic remarks do you make per week?  ")

while not response1.isnumeric():
    print("You must enter a positive whole number.")
    response1 = input("How many sarcastic remarks do you make per week?  ")

response1 = int(response1)

while response1 > 100:
    print("That's unlikely. Try a lower number.")
    response1 = int(input("How many sarcastic remarks do you make per week?  "))

# For right now, multiple choice responses are not checked to make sure they are in the valid range. It will be assumed that, if the user doesn't choose a given option, nothing will be added to their score (i.e. they are Rose).    
response2 = input("Your response to hearing someone you know say something ridiculous is:\nA. Change the subject\nB. Ask a serious follow-up question\nC. Eye roll\nD. Sarcastic jab\nEnter the letter you've chosen:  ").lower()

response3 = input("You are picking up a friend at their house and they can't seem to find their keys. You decide to:\nA. Start helping them look\nB. Pretend you're helping them look, but not really trying\nC. Ask what they look like\nD. Stand there and do nothing\nEnter the letter you've chosen:  ").lower()

if response1 > 20:
    score += 4
elif response1 <= 20 & response1 > 10:
    score += 3
elif response1 <= 10 & response1 > 5:
    score += 2
else:
    score += 1

if response2 == "a":
    score += 1
elif response2 == "c":
    score += 2
elif response2 == "d":
    score += 3

if response3 == "b":
    score += 1
elif response3 == "a":
    score += 2
elif response3 == "d":
    score += 3

if score < 3:
    print("You're Rose")
elif score >=3 and score < 6:
    print("You're Blanche")
elif score >= 6 and score < 9:
    print("You're Dorothy")
else:
    print("You're Sophia")

