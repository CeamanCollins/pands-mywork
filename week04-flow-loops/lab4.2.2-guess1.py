target = 30
guess = int(input("Please guess the number: "))

while guess != target:
    guess = int(input("Wrong\nPlease guess again: "))

print(f"Well done! Yes the number was {target}.")