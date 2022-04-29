#!/usr/bin/env python3

counter = 0
with open("345-0.txt", "r") as book:
    for line in book:
        if "vampire" in line.lower():
            counter += 1
            print(line)
print(f"The word 'vampire' appears {counter} times")

