import random

random_numbers = []
number_of_numbers = 10
range_to = 100

for i in range(number_of_numbers):
    random_numbers.append(random.randint(1,range_to))
print(f"Queue is {random_numbers}")
while random_numbers != []:
    print(f"Current number is {random_numbers[0]} and the queue is {random_numbers[1:]}")
    random_numbers.pop(0)
print("The queue is now empty")