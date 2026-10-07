"""
PYTHON PROGRAMMING COURSE
WEEK 1 - Python Basics & Control Structures

Assignments:
    1. Temperature Converter
    2. Student Grade Calculator
    3. Even/Odd & Prime Number Checker
Mini Project:
    "Simple ATM Simulator"

Run:  python week_1_assignments.py
"""


# ---------------------------------------------------------------------------
# Helper: safe numeric input
# ---------------------------------------------------------------------------
def get_number(prompt, as_int=False):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            value = input(prompt)
            return int(value) if as_int else float(value)
        except ValueError:
            print("  Invalid input. Please enter a number.")


# ---------------------------------------------------------------------------
# Assignment 1: Temperature Converter (Celsius <-> Fahrenheit)
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        c = get_number("Enter temperature in Celsius: ")
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == "2":
        f = get_number("Enter temperature in Fahrenheit: ")
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    else:
        print("Invalid choice.")


# ---------------------------------------------------------------------------
# Assignment 2: Student Grade Calculator
# ---------------------------------------------------------------------------
def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def student_grade_calculator():
    print("\n--- Student Grade Calculator ---")
    name = input("Enter student name: ").strip()
    count = get_number("How many subjects? ", as_int=True)

    if count <= 0:
        print("Number of subjects must be at least 1.")
        return

    marks = []
    for i in range(1, count + 1):
        while True:
            m = get_number(f"Enter marks for subject {i} (0-100): ")
            if 0 <= m <= 100:
                marks.append(m)
                break
            print("  Marks must be between 0 and 100.")

    average = calculate_average(marks)
    grade = assign_grade(average)

    print(f"\nStudent : {name}")
    print(f"Total   : {sum(marks):.2f} / {count * 100}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")


# ---------------------------------------------------------------------------
# Assignment 3: Even/Odd & Prime Number Checker
# ---------------------------------------------------------------------------
def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def number_checker():
    print("\n--- Even/Odd & Prime Number Checker ---")
    n = get_number("Enter an integer: ", as_int=True)

    print(f"{n} is {'Even' if is_even(n) else 'Odd'}.")
    print(f"{n} is {'a Prime' if is_prime(n) else 'not a Prime'} number.")


# ---------------------------------------------------------------------------
# Mini Project: Simple ATM Simulator
# ---------------------------------------------------------------------------
def check_balance(balance):
    print(f"\nCurrent balance: ₹{balance:.2f}")


def deposit(balance):
    amount = get_number("Enter amount to deposit: ")
    if amount <= 0:
        print("Deposit amount must be greater than 0.")
    else:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        check_balance(balance)
    return balance


def withdraw(balance):
    amount = get_number("Enter amount to withdraw: ")
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        check_balance(balance)
    return balance


def login(correct_pin, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == correct_pin:
            print("Login successful!")
            return True
        remaining = max_attempts - attempt
        print(f"Incorrect PIN. {remaining} attempt(s) left.")
    print("Too many failed attempts. Card blocked.")
    return False


def atm_simulator():
    print("\n--- Simple ATM Simulator ---")
    correct_pin = "1234"   # demo PIN
    balance = 5000.00      # starting balance

    if not login(correct_pin):
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------
def main():
    while True:
        print("\n=========== WEEK 1 - PYTHON ASSIGNMENTS ===========")
        print("1. Temperature Converter")
        print("2. Student Grade Calculator")
        print("3. Even/Odd & Prime Number Checker")
        print("4. Mini Project: Simple ATM Simulator")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            student_grade_calculator()
        elif choice == "3":
            number_checker()
        elif choice == "4":
            atm_simulator()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
