# floor.py
# author: Céaman Collins
# script that takes in a float and outputs an int rounded down

#imports
import math

input_value = float(input("Enter a float number: "))
floored_value = math.floor(input_value)
print(f"{input_value} floored is {floored_value}")