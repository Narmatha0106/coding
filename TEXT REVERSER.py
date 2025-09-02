# Text Reverser Program

def reverse_text(text):
    return text[::-1]  # Slicing technique to reverse the string

# Get input from user
user_input = input("Enter text to reverse: ")

# Display reversed text
print("Reversed text:", reverse_text(user_input))
