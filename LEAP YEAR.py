def is_leap_year(year):
    # Leap year if divisible by 4 and not by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    print("Leap Year Checker 🗓️")
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year ✅")
        else:
            print(f"{year} is not a leap year ❌")
    except ValueError:
        print("Please enter a valid numeric year.")

if __name__ == "__main__":
    main()
