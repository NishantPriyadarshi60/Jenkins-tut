# Simple Python Greeting Program

# Ask the user for their name
# name = input("What is your name? ")

# Greet the user
# print("Hello, " + name + "! Welcome!")



# user.py

import os
print("Hello, Nishant!")
name = os.environ.get("USERNAME", "DefaultUser")
print(f"Hello, {name}!")
