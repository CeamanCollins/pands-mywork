value = round(float((input("Enter the percentage: "))))
if value < 0 or value > 100:
    print("Please enter a number between 0 and 100.")
elif value < 40:
    print("Fail")
elif value < 50:
    print("Pass")
elif value < 60:
    print("Merit 2")
elif value < 70:
    print("Merit 1")
else:
    print("Distinction")