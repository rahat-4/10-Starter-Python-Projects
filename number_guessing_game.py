from random import randint

# Start the program with basic setup
lower_number, higher_number = 1, 10
random_number: int = randint(lower_number, higher_number)

print(f"Guess the number in the range from 1 to 10.")

# Run an infinite loop for the game
while True:
    # Get the user's guess
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check the user's guess
    if user_guess < random_number:
        print(f"Your guess is too low.")
    elif user_guess > random_number:
        print(f"Your guess is too high.")
    else:
        print(f"Congrats! You guessed it!")
        break
