import random

#1. take user input and print it

name1 = input("Hello there! what's your name? ")
name = "mystic python"

print(f"Hi {name1} !!")

"""
    python command to get pydoc of a module 
    e.g. "python3 -m pydoc random" 
    or pydoc print or pydoc random, etc. in terminal
"""
# 2. random number

random_number = random.randrange(0, 10, 4)

print(f"Random number is {random_number}")
