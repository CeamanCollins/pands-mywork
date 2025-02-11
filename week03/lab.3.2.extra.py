# extra.py
# author: Céaman Collins
# script to take in a float amount of dollars and returns that absolute amount in cent

input_value = float(input("Please enter an amount: "))
absolute_value_as_cent = round(abs(input_value)*100)
print(f"That amount in cent is: {absolute_value_as_cent}")

# or

# absolute_value_as_cent = abs(input_value)*100
# print(f"That amount in cent is: {absolute_value_as_cent:.0f}")