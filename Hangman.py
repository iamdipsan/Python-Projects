import random
from word_list import words  # Import the words from word_list.py file

def hangman():
    random_word = random.choice(words)  # Generate the random word
    print(random_word)  # Print the chosen word for testing purposes; remove in production
    
    word_display = ["_"] * len(random_word)  # Create blank lines "_" equal to the length of the word. Example: If the word is "cow", display _ _ _
    guessed_letters = []  # Empty list to store the letters that have been guessed
    lives = 5  # Number of lives for the player

    print("Welcome to Hangman!")  # Print welcome statement
    print(" ".join(word_display))  # Display the current state of the word, which is all empty. Join the list elements into a single string with spaces between

    while lives > 0:  # The game continues to run as long as the player has more than 0 lives
        user_guess = input("Enter a single letter for your guess: ").lower()  # Asks the player to input a letter and convert it to lowercase
        
        # Check whether the player entered a valid input
        # The conditions check if they entered more than one letter or if the input is not an alphabetical letter (e.g., number)
        # If invalid, skip the loop and ask again
        # If valid, continue
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        # This checks whether the player has already guessed the same letter before
        # If so, the game asks the player to try a different letter
        if user_guess in guessed_letters:
            print(f"You've already guessed '{user_guess}'. Try another guess.")
            continue
        
        # Adds the guessed letter to the guessed_letters list so it can be checked later for repeated guesses
        guessed_letters.append(user_guess)

        # Check if the guessed letter is in the random_word
        # Checks if the guessed letter is part of the randomly chosen word
        if user_guess in random_word:
            # Loops through each letter in random_word and its index
            for index, letter in enumerate(random_word):
                if letter == user_guess:  # If the current letter matches the player's guess, the corresponding underscore in word_display is replaced by the guessed letter
                    word_display[index] = user_guess
            print("Good guess!")  # Print a message for a correct guess
        else:
            lives -= 1  # Reduces the number of remaining lives by 1 for an incorrect guess
            print(f"Wrong guess! Remaining lives: {lives}")

        # Displays the current state of the word (with guessed letters filled in and remaining letters as underscores)
        print(" ".join(word_display))

        # Check if there are no underscores left in word_display, meaning the player has successfully guessed all letters in the word
        if "_" not in word_display:
            print("Congratulations, you guessed the word!")  # Display congratulations message
            break  # Exit the loop since the game is over
    else:
        # This runs if no lives are left
        print(f"You have run out of lives. The word was: {random_word}")

hangman()  # Function to start the game
