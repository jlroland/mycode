#!/usr/bin/env python3
import random

icecream= ["indentation", "spaces"]
tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

icecream.append(4)
#student_id= int(input("Choose a number between 0 and 17: "))
student_id= random.randint(0,17)

print(f"{tlgstudents[student_id]} always uses {icecream[2]} {icecream[1]} to indent.")

