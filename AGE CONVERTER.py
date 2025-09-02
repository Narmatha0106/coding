from datetime import datetime

def calculate_age(birthdate_str):
    # Convert string to datetime object
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.today()

    # Calculate age
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# Input from user
birthdate_input = input("Enter your birthdate (DD-MM-YYYY): ")
try:
    age = calculate_age(birthdate_input)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY.")
