# Task 2: Check whether an integer is even or odd and whether it is
# divisible by 3 and 5.

def check_number(number):
    return {
        "Even": number % 2 == 0,
        "Divisible by 3": number % 3 == 0,
        "Divisible by 5": number % 5 == 0,
    }


def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    results = check_number(number)
    parity = "Even" if results["Even"] else "Odd"
    print(f"Number is {parity}.")
    print(f"Divisible by 3: {'Yes' if results['Divisible by 3'] else 'No'}")
    print(f"Divisible by 5: {'Yes' if results['Divisible by 5'] else 'No'}")


if __name__ == "__main__":
    main()