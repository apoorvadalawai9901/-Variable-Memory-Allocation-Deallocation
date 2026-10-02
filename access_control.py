# Task 7: Grant access when age >= 18 and the person has an ID,
# or when the person is an employee.

def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


def read_yes_no(prompt):
    answer = input(prompt).strip().lower()
    if answer not in ("yes", "no"):
        raise ValueError("Please answer yes or no.")
    return answer == "yes"


def main():
    try:
        age = int(input("Enter age: "))
        has_id = read_yes_no("Do you have an ID? (yes/no): ")
        is_employee = read_yes_no("Are you an employee? (yes/no): ")
        
    except ValueError as error:
        print(error)
        return

    print(check_access(age, has_id, is_employee))


if __name__ == "__main__":
    main()