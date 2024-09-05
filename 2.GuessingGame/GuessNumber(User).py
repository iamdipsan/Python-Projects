# This program is a simple number guessing game.
# The user is asked to guess a randomly generated number between 1 and a specified upper limit.
# The program provides feedback on whether the guess is too high or too low.
# The game continues until the user guesses the correct number.
# It handles invalid inputs by prompting the user to enter a valid integer.

import random  # Import the random module to use its functions for generating random numbers

def guess_random_number(number):
    """
    Function to allow the user to guess a random number between 1 and the specified `number`.

    This function generates a random integer between 1 and the provided `number` (inclusive).
    It then repeatedly prompts the user to guess the random number, providing feedback on whether
    the guess is too high or too low, until the correct number is guessed. The function handles
    invalid inputs by catching exceptions and informing the user to enter a valid integer.
    """
    # Generate a random number between 1 and the specified `number` (inclusive)
    random_number = random.randint(1, number)
    guess = None  # Initialize the variable `guess` to None before starting the loop

    # Loop until the user guesses the correct number
    while guess != random_number:
        try:
            # Prompt the user to enter a number between 1 and `number`
            guess = int(input(f"Enter a number between 1 and {number}: "))
            
            # Provide feedback based on whether the guess is too low or too high
            if guess < random_number:
                print("Too low, guess a greater number.")
            elif guess > random_number:
                print("Too high, guess a smaller number.")
        
        except ValueError:
            # Handle the case where the user inputs something that isn't an integer
            print("Invalid input. Please enter a valid integer.")

    # Congratulate the user once they guess the correct number
    print("You have guessed the random number correctly. Congrats!")

# Call the function with an upper limit of 10
guess_random_number(10)
