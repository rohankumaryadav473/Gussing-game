import random

print(" Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")