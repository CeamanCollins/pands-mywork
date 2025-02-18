import random

list = []

for i in range(11):
    list.append(random.randint(0, 100))

sorted_list = sorted(list)

print(f"10 random numbers are \t{list}")
print(f"The top 3 are \t\t {sorted_list[-3:]}")