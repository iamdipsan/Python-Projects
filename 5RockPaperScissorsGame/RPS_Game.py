import random  # Import the random module to generate random choices for the computer.

def playGame():
    while True:  # Infinite loop to keep the game running until the user decides to stop.
        # Ask the user to enter their choice and convert it to lowercase.
        user_choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()

        # Check if the user input is valid (i.e., 'r', 'p', or 's').
        if user_choice not in ['r', 'p', 's']:
            print("Invalid Input. Please try again.")
            continue  # If the input is invalid, restart the loop.

        print(f"You chose {user_choice}")  # Display the user's choice.

        # Computer randomly picks one of the choices ('r', 'p', 's').
        computer_choice = random.choice(['r', 'p', 's'])
        print(f"The computer chose {computer_choice}")  # Display the computer's choice.

        # Check if the user's choice is the same as the computer's choice.
        if user_choice == computer_choice:
            print("It's a tie.")  # It's a tie if both choices are the same.
        elif _iswinner(user_choice, computer_choice):
            print("You won!")  # The user wins if their choice beats the computer's choice.
        else:
            print("You lost.")  # The user loses if the computer's choice beats theirs.

        # Ask the user if they want to play again.
        play_again = input("Do you want to play again? Enter 'yes' or 'no': ").strip().lower()

        # If the user doesn't enter 'yes', end the game.
        if play_again != 'yes':
            print("Thank you for playing!")  # Thank the user for playing.
            break  # Exit the loop and end the game.

def _iswinner(user, computer):
    # Determine if the user's choice beats the computer's choice.
    # Rock ('r') beats Scissors ('s'), Scissors ('s') beat Paper ('p'), Paper ('p') beats Rock ('r').
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True  # Return True if the user wins.

# Start the game by calling the playGame function.
playGame()
