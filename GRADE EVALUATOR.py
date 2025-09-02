def evaluate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    print("📚 Grade Evaluator")
    try:
        marks = float(input("Enter your marks (0–100): "))
        if 0 <= marks <= 100:
            grade = evaluate_grade(marks)
            print(f"Your grade is: {grade}")
        else:
            print("❌ Marks should be between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
