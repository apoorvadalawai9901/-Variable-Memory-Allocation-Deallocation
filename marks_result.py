# Task 3: Return Pass for marks >= 35, Fail otherwise, and Distinction
# for marks >= 75.

def get_result(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"


def main():
    try:
        marks = float(input("Enter the student's marks: "))
    except ValueError:
        print("Please enter valid marks.")
        return

    print(get_result(marks))


if __name__ == "__main__":
    main()