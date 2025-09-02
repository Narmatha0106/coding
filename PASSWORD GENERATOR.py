import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Combine all characters
    all_chars = letters + digits + punctuation

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for desired password length
try:
    user_length = int(input("Enter desired password length: "))
    if user_length < 4:
        print("Password should be at least 4 characters long.")
    else:
        print("Generated Password:", generate_password(user_length))
except ValueError:
    print("Please enter a valid number.")
