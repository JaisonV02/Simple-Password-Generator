# Import string to be able to return characters
# Import random to be able to select random characters from string library
import string
import random

# Function to generate and return a password
def generate(length, uppercase, number, special):

    # Create an integer which identifies the password requirements
    requirements = [uppercase, number, special]
    requirements = [str(i) for i in requirements]
    requirements = int(''.join(requirements))

    # If user only wants lowercase letters
    if requirements == 0:
        password = ''.join([random.choice(string.ascii_lowercase) for i in range(length)])
        return password
    
    # If user wants uppercase letters
    elif requirements == 100:
        password = ''.join([random.choice(string.ascii_letters) for i in range(length)])
        return password
    
    # If user wants numbers
    elif requirements == 10:
        password = ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(length)])
        return password
    
    # If user wants special characters
    elif requirements == 1:
        password = ''.join([random.choice(string.ascii_lowercase + string.punctuation) for i in range(length)])
        return password
    
    # If user wants both uppercase letters and numbers
    elif requirements == 110:
        password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])
        return password
    
    # If user wants both uppercase letters and special characters
    elif requirements == 101:
        password = ''.join([random.choice(string.ascii_letters + string.punctuation) for i in range(length)])
        return password
    
    # If user wants both numbers and special characters
    elif requirements == 11:
        password = ''.join([random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(length)])
        return password
    
    # If user has selected all the requirements for a password
    elif requirements == 111:
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)])
        return password
