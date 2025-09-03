# Multiplication Table Generator

# Ask the user for input
num = int(input("Enter a number to display its multiplication table: "))

# Define the range of the table (1 to 10)
print(f"\nMultiplication Table for {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
