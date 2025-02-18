# randomfruit.py
# author: Céaman Collins
# script to return a random fruit from a list

import random

fruits = ["orange", "banana", "apple", "kiwi", "melon"]
# not great for readability
# print(f"A random fruit: {fruits[random.randint(0,len(fruits)-1)]}")

# easier readability
# index = random.randint(0,len(fruits)-1)
# fruit = fruits[index]

# print(f"A radnom fruit: {fruit}") 

# simplest solution
random_fruit = random.choice(fruits)
# source https://www.w3schools.com/python/module_random.asp

print(f"A random fruit: {random_fruit}")