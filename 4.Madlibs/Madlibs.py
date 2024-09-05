

#For those who dont know what a madlib is,
# A Mad Libs game is a word game that involves creating a humorous story by filling in the blanks with words. 
#Lets create this game step wise step.
#The first thing is we need to a story for filling in the blanks.
#I have created a simple Introduction  .
#lets break the steps down.Lets create variables that stores the words for filling the story, in this case,  the words  are
#name,ages, adress, work ,is_Happy.These are the variables that will store the data that the user inputs.
#The user takes the input asking them their name,age,address,adress, work ,is_Happy then the data are stored in the respective variables.
name = input("Enter a name: ")
age= input("Enter you age: ")
address = input("Enter where you live: ")
work = input("Enter your work ie your job : ")
is_happy = input("Enter wether you are happy with your work or not ie Happy or notHappy: ")
#we create story here and store the story in a variable named madlibs. 
# using string concatenation, in this case we are using the f string.
#we pace the input that the user inputs using {}.
#the variables are replaced by the actual info.
#The final step is to print the madlib and play the Game.
madlib = f"Hey there! My Name is {name}.I'm {age} years old. I live in {address}.I work at {work} & I'm very happy with my life."

print(madlib)

#Feel free to create your own fun madlibs.


