# Task 9: Calculate using +, -, *, /, //, %, or **. Handle invalid
# operators and division by zero.

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator in ("/", "//", "%") and b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    if operator == "/":
        return a / b
    if operator == "//":
        return a // b
    if operator == "%":
        return a % b
    if operator == "**":
        return a ** b
    raise ValueError("Invalid operator. Use +, -, *, /, //, %, or **.")


def main():
    try:
        a = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
        b = float(input("Enter the second number: "))
        print(f"Result: {calculate(a, operator, b)}")
    except (ValueError, ZeroDivisionError) as error:
        print(error)


if __name__ == "__main__":
    main()