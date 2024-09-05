import random  # Import the random module for shuffling

print("Welcome to the Quiz Game")  # Print welcome message

wanna_play = input("Do you want to play the game (yes/no): ").lower()  # Ask if the user wants to play

if wanna_play != 'yes':  # If user does not want to play, quit
    quit()

print("Okay, then! Let's play")  # Print message to start the game

# Creating a list of tuples containing questions and answers 
question_answer_pairs = [
    ("What does CPU stand for?", "Central Processing Unit"),
    ("Which programming language is known as the 'mother of all languages'?", "C"),
    ("What does HTML stand for?", "HyperText Markup Language"),
    ("In which year was Python first released?", "1991"),
    ("Which company developed the Windows operating system?", "Microsoft"),
    ("What is the main purpose of a compiler?", "To translate source code into machine code"),
    ("Which database management system is known for its SQL language?", "MySQL"),
    ("What does 'HTTP' stand for?", "HyperText Transfer Protocol"),
    ("What is the most popular web server software?", "Apache"),
    ("Which algorithm is used for data encryption in modern security systems?", "AES (Advanced Encryption Standard)"),
    ("What does 'GUI' stand for in software development?", "Graphical User Interface"),
    ("Which company created the Android operating system?", "Google"),
    ("What is the primary function of an operating system?", "To manage hardware and software resources"),
    ("Which language is known for its use in web development and is often associated with front-end development?", "JavaScript"),
    ("What does 'API' stand for?", "Application Programming Interface"),
    ("Which technology is used for creating virtual private networks (VPNs)?", "IPsec (Internet Protocol Security)"),
    ("What is the purpose of the 'git' version control system?", "To track changes in source code and manage version history"),
    ("What does 'DNS' stand for?", "Domain Name System"),
    ("Which programming language is known for its use in data science and machine learning?", "Python"),
    ("What is the name of the open-source operating system based on Unix?", "Linux")
]

# Shuffle the list of tuples to ensure random order
random.shuffle(question_answer_pairs)

score = 0

# Iterate through the shuffled list of tuples 
#for each question and answer in question_answer_pairs
#ask the user answer for  the question
#if the useranswer matches  with the answer   in the tuple
#print correct and update and print score
#if it doest matches the answer, decrease the score and continue
for question, correct_answer in question_answer_pairs:
    user_answer = input(f"{question} ").strip()  # Ask the question and get user input

    if user_answer.lower() == correct_answer.lower():  # Check if the answer is correct
        print("Correct answer")
        score += 1  # Increase score for a correct answer
    else:
        print(f"Incorrect answer. The correct answer is: {correct_answer}")
        score -= 1  # Decrease score for an incorrect answer

    print(f"Current Score: {score}")

#print the  score
print(f"Quiz over! Your final score is {score}/{len(question_answer_pairs)}")
