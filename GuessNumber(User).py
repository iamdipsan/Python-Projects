# This program is a number guessing game where the computer attempts to guess a number
# that the user has chosen within a specified range. The user provides the lower and upper
# bounds of the range and selects a number for the computer to guess. The computer uses a
# binary search approach to guess the number, and the user provides feedback to guide the
# computer's guesses until it finds the correct number or determines that it is outside the range.

import random  # Import the random module for generating random numbers.
#we are not using this for now.

def guess_number():
    """
    Function where the computer attempts to guess a number chosen by the user within a specified ranges.
    
    The user defines the lower and upper bounds of the range and provides a number for the computer to guess.
    The computer uses a binary search approach to guess the number and the user provides feedback to guide it.
    """
    # Get the lower bound of the range from the user
    low = int(input("Enter the lower range: "))
    # Get the upper bound of the range from the user
    high = int(input("Enter the higher range: "))

    # Check if the provided range is valid
    if low >= high:
        print("Invalid range. The higher range must be greater than the lower range.")
        return  # Exit the function if the range is invalid

    # Get the number from the user that the computer will attempt to guess
    Your_number = int(input(f"Enter your number for the computer to guess between {low} and {high}: "))

    # Check if the number entered by the user is within the specified range
    if Your_number < low or Your_number > high:
        print("The number you entered is out of the specified range.")
        return  # Exit the function if the number is out of the range

    # Initialize the computer's guess variable
    computer_guess = None

    # Loop until the computer guesses the correct number
    while computer_guess != Your_number:
        # Compute the computer's guess as the midpoint of the current range
        computer_guess = (low + high) // 2
        print(f"The computer guesses: {computer_guess}")

        # Get feedback from the user about the computer's guess
        feedback = input(f"Is {computer_guess} too low, too high, or correct? (Enter 'h' for higher, 'l' for lower, 'c' for correct): ").strip().lower()
        
        # Process the user's feedback to adjust the guessing range
        if feedback == 'c':
            if computer_guess == Your_number:
                print("The computer guessed your number correctly! Congrats!")
                return  # Exit the function once the correct number is guessed
            else:
                continue  
        elif feedback == 'h':
            high = computer_guess - 1  #if the guess is too high, lower the upper range.
        elif feedback == 'l': #if the guess is two low, increase the lower range.
            low = computer_guess + 1  
        else:
            print("Invalid feedback, please enter 'h', 'l', or 'c'.")  # Handle invalid feedback

# Call the function to start the guessing game
guess_number()
