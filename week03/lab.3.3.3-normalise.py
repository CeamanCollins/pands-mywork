# normalise.py
# author: Céaman Collins
# script to read in a string and strip any leading or trailing spaces, convert the string to lower case 
# and output the length of the input and output strings

message = input("Please enter a string:")
message_normalised = message.strip().lower()
lenth_of_message = len(message)
length_of_message_normalised = len(message_normalised)
print(f"That string normalised is: {message_normalised}")
print(f"We reduced the input string from {lenth_of_message} to {length_of_message_normalised} characters.")