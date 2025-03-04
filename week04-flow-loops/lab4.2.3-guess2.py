import random

target = random.randint(1, 100)
guess = int(input("Please guess the number: "))

while guess != target:
    if guess > target:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Please guess again: "))

print(f"Well done! Yes the number was {target}.")