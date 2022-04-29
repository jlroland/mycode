#!/usr/bin/env python3
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
choices = ["B","C","D"]

print(trivia["question"])
print("A.  "+html.unescape(trivia["correct_answer"]))
for i in range(len(choices)):
    answer = html.unescape(trivia["incorrect_answers"][i])
    print(f"{choices[i]}.  {answer}")

response = input("Your answer --> ")

if response.lower() == "a":
    print("Correct!")
else:
    print("Incorrect. The answer is A.")


