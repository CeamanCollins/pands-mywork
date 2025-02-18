value = 1
list = []
while value != 0:
    value = int(input("Enter a number (0 to quit)"))
    if value != 0:
        list.append(value)
for i in list:
    print(i)
average = sum(list) / len(list)
print(f"The average is {average}")
