value = 0
while value != -1:
    value = int(input("Enter a number: "))
    if value % 2:
        print (f"{value} is an odd number")
    else:
        print(f"{value} is an even number")