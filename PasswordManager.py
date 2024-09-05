# Importing the Fernet module from the cryptography library
from cryptography.fernet import Fernet

# The write_key function generates an encryption key and saves it to a file.
# It's currently commented out, but you need to run it once to create the 'key.key' file.
'''
def write_key():
    # Generates a new key using Fernet
    key = Fernet.generate_key()

    # Writes the key to the 'key.key' file in binary mode
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# This function loads the encryption key from the 'key.key' file.
# The encryption key is necessary for encrypting and decrypting passwords.
def load_key():
    # Opens the 'key.key' file in read binary mode
    file = open("key.key", "rb")
    
    # Reads the key from the file and stores it in the 'key' variable
    key = file.read()
    
    # Closes the key file after reading it
    file.close()
    
    # Returns the encryption key to be used later
    return key

# The key is loaded from the file and stored in the 'key' variable
key = load_key()

# The Fernet object 'fer' is created using the loaded key.
# This object will be used to encrypt and decrypt data.
fer = Fernet(key)

# Function to view stored passwords in the 'passwords.txt' file
def view():
    # Opens the 'passwords.txt' file in read mode
    with open('passwords.txt', 'r') as f:
        
        # Reads each line of the file
        for line in f.readlines():
            # Removes trailing characters like newline from the line
            data = line.rstrip()
            
            # Splits the line by the "|" separator to get the username and encrypted password
            user, passw = data.split("|")
            
            # Decrypts the password using the Fernet object 'fer', encodes it, and then decodes it back to plain text
            decrypted_password = fer.decrypt(passw.encode()).decode()
            
            # Prints the username and the decrypted password
            print("User:", user, "| Password:", decrypted_password)

# Function to add new account names and passwords to the 'passwords.txt' file
def add():
    # Takes input from the user for account name
    name = input('Account Name: ')
    
    # Takes input from the user for the password
    pwd = input("Password: ")

    # Opens the 'passwords.txt' file in append mode, allowing new lines to be added without overwriting existing content
    with open('passwords.txt', 'a') as f:
        
        # Encrypts the password using the Fernet object 'fer', encodes it to bytes, and then decodes it back to a string
        encrypted_password = fer.encrypt(pwd.encode()).decode()
        
        # Writes the account name and the encrypted password to the file in the format 'account_name|encrypted_password'
        f.write(name + "|" + encrypted_password + "\n")

# Main loop to ask the user what they want to do: view passwords, add new passwords, or quit
while True:
    # Prompts the user to choose between viewing passwords, adding a new one, or quitting the program
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    
    # If the user enters 'q', the program will exit the loop and stop running
    if mode == "q":
        break

    # If the user selects 'view', the view function is called to display stored passwords
    if mode == "view":
        view()
        
    # If the user selects 'add', the add function is called to add a new password
    elif mode == "add":
        add()
        
    # If the user enters an invalid option, the program tells them it's invalid and continues to prompt for input
    else:
        print("Invalid mode.")
        continue
