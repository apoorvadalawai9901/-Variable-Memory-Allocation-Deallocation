# Task 5: Validate a user only when username is "admin" and
# password is "python123".

def validate_user(username, password):
    return username == "admin" and password == "python123"


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_user(username, password):
        print("Valid user")
    else:
        print("Invalid username or password")


if __name__ == "__main__":
    main()