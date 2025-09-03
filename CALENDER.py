import calendar

# Ask the user for month and year
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Display the calendar
print("\nHere’s your calendar:\n")
print(calendar.month(year, month))
