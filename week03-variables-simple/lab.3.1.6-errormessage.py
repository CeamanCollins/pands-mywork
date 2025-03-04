# errormessage.py
# author: Céaman Collins
# script to investigate an error and fix it

# The following returns TypeError: can only concatenate str (not "int") to str
# message = 'I have eaten ' + 99 + ' burritos.'
# print(message)

#converting the number to a string makes them concatenatable
message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# answer to question 7
# because a variable name cannot start with a number

# answer to question 8
# value = 99
# print(f"{int(value)}")
# print(f"{float(value)}")
# print(f"{str(value)}")