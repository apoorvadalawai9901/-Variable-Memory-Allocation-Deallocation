# Task 1: Calculate addition, subtraction, multiplication, division,
# floor division, and remainder for two numbers.

def calculate(first_number, second_number):
    if second_number == 0:
        division_results = {
            "Division": "undefined (cannot divide by zero)",
            "Floor division": "undefined (cannot divide by zero)",
            "Remainder": "undefined (cannot divide by zero)",
        }
    else:
        division_results = {
            "Division": first_number / second_number,
            "Floor division": first_number // second_number,
            "Remainder": first_number % second_number,
        }

    return {
        "Addition": first_number + second_number,
        "Subtraction": first_number - second_number,
        "Multiplication": first_number * second_number,
        **division_results,
    }


def main():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    for operation, result in calculate(first_number, second_number).items():
        print(f"{operation}: {result}")


if __name__ == "__main__":
    main()