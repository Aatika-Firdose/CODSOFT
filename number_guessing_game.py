import random

print("Welcome to Number Guessing Game!")

# Generate a random number between 1 and 100
number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1 to 100): "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break
    except ValueError:
        print("Please enter a valid number.")
