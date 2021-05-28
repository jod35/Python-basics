"""
Create a simple program that is going to prompt 
a user for their name as an argument variable. Let it also prompt them
for the following 

- age 
- type of computer they are using

Let the output of the program be 

'Hey Jonathan, you are 12 years old and are using a Mac Book'

"""

import sys

script,username=sys.argv

age=int(input("Enter your age: "))

type_of_computer=input("Enter the type of computer you are using: ")

print(f"Hey {username}, you are {age} years old and are using a {type_of_computer}")

