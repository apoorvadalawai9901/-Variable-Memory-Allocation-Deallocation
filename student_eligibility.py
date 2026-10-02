# Task 4: A student is eligible when marks >= 60, attendance >= 75,
# and the student has no backlog.

def check_eligibility(marks, attendance, has_backlog):
    if marks >= 60 and attendance >= 75 and not has_backlog:
        return "Eligible"
    return "Not eligible"


def main():
    try:
        marks = float(input("Enter the student's marks: "))
        attendance = float(input("Enter the attendance percentage: "))
    except ValueError:
        print("Please enter valid numbers for marks and attendance.")
        return

    backlog_input = input("Does the student have a backlog? (yes/no): ").strip().lower()
    if backlog_input not in ("yes", "no"):
        print("Please enter yes or no for backlog status.")
        return

    has_backlog = backlog_input == "yes"
    print(check_eligibility(marks, attendance, has_backlog))


if __name__ == "__main__":
    main()