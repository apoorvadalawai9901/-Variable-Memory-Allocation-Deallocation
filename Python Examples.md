# Python Examples

This guide explains every Python file found in the workspace folder and its subfolders. The inventory contains 10 Python files, all in the current folder. Each file has one program. The source code below is reproduced from the files; explanations follow it. No `.py` file was changed to create this guide.

## 1. `calculator.py`

### Program name and purpose

**Arithmetic calculator.** It calculates addition, subtraction, multiplication, division, floor division, and remainder for two numbers.

### What it does

The program asks for two numbers and prints all six results. Division, floor division, and remainder need a nonzero second number. If the second number is zero, the program prints an explanation for those three results and still prints addition, subtraction, and multiplication.

### Code

```python
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
```

### Line-by-line explanation

- The `#` lines are comments for people reading the code. Python does not execute them.
- `def calculate(first_number, second_number):` defines a function. `first_number` and `second_number` are parameters: names that receive the values supplied to the function.
- `if second_number == 0:` checks whether the second number equals zero. `==` compares values; it does not assign a value.
- The first dictionary stores text for division results that cannot be calculated when the divisor is zero.
- `else:` runs when the second number is not zero. Its dictionary calculates `/` (division), `//` (floor division), and `%` (remainder).
- `return { ... }` sends a dictionary back to the caller. The dictionary includes addition with `+`, subtraction with `-`, multiplication with `*`, and the three values from `division_results`.
- `**division_results` here copies dictionary entries into another dictionary. In Task 9, `**` is instead the exponentiation operator.
- `def main():` defines the part that interacts with the user.
- `try:` starts a block where an input conversion might fail.
- `input(...)` displays a prompt and reads text. `float(...)` converts that text to a decimal number, so inputs such as `2.5` are accepted.
- `except ValueError:` handles text that cannot be converted to a number. The message is printed and `return` exits `main()` early.
- `for operation, result in ...items():` loops through each key and value in the returned dictionary. A loop repeats its indented body once per dictionary item.
- `print(f"{operation}: {result}")` displays each pair. The `f` before the string lets Python insert the variable values inside `{}`.
- `if __name__ == "__main__":` checks whether this file was run directly. If true, it calls `main()`. If another file imports this file, the prompt does not start automatically.

### How it works

1. The program asks for the first number and converts it to `float`.
2. It asks for the second number and converts it to `float`.
3. `main()` calls `calculate()` with both values as arguments.
4. `calculate()` checks for zero, performs the available calculations, and returns a dictionary.
5. The `for` loop prints every operation and result.

### Example

Input:

```text
Enter the first number: 10
Enter the second number: 3
```

Expected output:

```text
Addition: 13.0
Subtraction: 7.0
Multiplication: 30.0
Division: 3.3333333333333335
Floor division: 3.0
Remainder: 1.0
```

### Important concepts

- `float()` converts input text into a number that may contain a decimal part.
- `/`, `//`, and `%` need a nonzero second number.
- A dictionary stores named values as key/value pairs.
- `return` sends a value back; it does not display it by itself.
- `for` repeats code for each item in a collection.
- `try` and `except` let the program respond to invalid numeric input.

---

## 2. `number_check.py`

### Program name and purpose

**Even, odd, and divisibility checker.** It checks one integer for evenness and divisibility by 3 and 5.

### What it does

The function returns three `True` or `False` answers. The main program turns those answers into readable output.

### Code

```python
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
```

### Line-by-line explanation

- `def check_number(number):` defines a function with one parameter, `number`.
- The function returns a dictionary with three tests.
- `number % 2` finds the remainder after dividing by 2. `== 0` checks if that remainder is zero. A number with no remainder when divided by 2 is even.
- The next two entries use the same idea for 3 and 5.
- `def main():` defines the input/output part of the program.
- `int(input(...))` reads text and converts it to a whole number. A decimal such as `2.5` is not a valid integer for `int()`.
- `except ValueError:` handles input such as `hello`. `return` stops `main()` after printing the error message.
- `results = check_number(number)` calls the function and stores its dictionary in `results`.
- `"Even" if results["Even"] else "Odd"` is a conditional expression. It chooses `Even` when the value is true and `Odd` when it is false.
- The remaining `print()` calls use conditional expressions to convert Boolean values into `Yes` or `No`.
- The final `if __name__ ...` block runs `main()` only when this file is started directly.

### How it works

1. The program asks for a whole number.
2. It checks each remainder: divide by 2, 3, and 5.
3. The function returns the three Boolean results.
4. The program displays even/odd and yes/no messages.

### Example

Input:

```text
Enter an integer: 15
```

Expected output:

```text
Number is Odd.
Divisible by 3: Yes
Divisible by 5: Yes
```

### Important concepts

- `%` is the remainder operator.
- `==` compares two values and returns `True` or `False`.
- `int()` converts input into a whole number.
- A Boolean value is either `True` or `False`.
- A conditional expression has the form `value_if_true if condition else value_if_false`.

---

## 3. `marks_result.py`

### Program name and purpose

**Student marks result checker.** It returns a grade label based on the student's marks.

### What it does

Marks of 75 or more receive `Distinction`. Marks from 35 up to 75 receive `Pass`. Anything below 35 receives `Fail`.

### Code

```python
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
```

### Line-by-line explanation

- `def get_result(marks):` defines a function that receives marks as a parameter.
- `if marks >= 75:` checks the highest threshold first. `>=` means greater than or equal to.
- `return "Distinction"` sends the result back immediately and ends the function.
- The second `if` runs only if the first one did not return. It checks the pass threshold.
- If both conditions are false, `return "Fail"` is reached.
- `main()` reads marks as a `float`, allowing decimal marks.
- `try`/`except ValueError` prevents invalid text from stopping the program with a traceback.
- `print(get_result(marks))` calls the function and displays the returned string.
- The final guard starts `main()` when the file is run directly.

### How it works

1. The program reads marks and converts them to a number.
2. It checks for distinction first.
3. If not distinction, it checks for pass.
4. If neither threshold is met, it returns fail.
5. The result is printed.

### Example

Input:

```text
Enter the student's marks: 75
```

Expected output:

```text
Distinction
```

### Important concepts

- `if` runs indented code only when its condition is true.
- `return` exits the function immediately.
- The order of conditions matters when the thresholds overlap.
- No range validation is present, so values above 100 still return `Distinction`, and negative marks return `Fail`.

---

## 4. `student_eligibility.py`

### Program name and purpose

**Student eligibility checker.** It checks marks, attendance, and backlog status.

### What it does

The student is eligible only when marks are at least 60, attendance is at least 75%, and the student has no backlog.

### Code

```python
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
```

### Line-by-line explanation

- `check_eligibility` has three parameters: marks, attendance, and a Boolean backlog flag.
- `marks >= 60` checks the mark requirement.
- `attendance >= 75` checks the attendance requirement.
- `not has_backlog` is true when the backlog value is false.
- `and` means every condition must be true. If all pass, the function returns `Eligible`; otherwise it returns `Not eligible`.
- In `main()`, marks and attendance are read as decimal numbers using `float()`.
- If either conversion fails, the `except ValueError` block prints an error and returns from `main()`.
- `.strip()` removes spaces from the beginning and end of the backlog answer. `.lower()` changes letters to lowercase.
- `backlog_input not in ("yes", "no")` checks that the answer is one of the two allowed words. Parentheses here create a tuple.
- `backlog_input == "yes"` creates a Boolean: yes becomes `True`, no becomes `False`.
- The function call passes three arguments to the three parameters; `print()` displays its return value.

### How it works

1. It reads marks and attendance.
2. It reads and validates the yes/no backlog response.
3. It converts that response into `True` or `False`.
4. The function tests all three requirements with `and`.
5. The program prints the eligibility result.

### Example

Input:

```text
Enter the student's marks: 60
Enter the attendance percentage: 75
Does the student have a backlog? (yes/no): no
```

Expected output:

```text
Eligible
```

### Important concepts

- `and` requires every joined condition to be true.
- `not` reverses a Boolean value.
- `in` and `not in` check for membership in a collection.
- `strip()` and `lower()` are string methods.
- Boolean values are `True` and `False`; they are not the strings `"true"` and `"false"`.

---

## 5. `user_validation.py`

### Program name and purpose

**Username and password check.** It compares the entered values with one required username and password.

### What it does

The user is accepted only when the username is exactly `admin` and the password is exactly `python123`.

### Code

```python
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
```

### Line-by-line explanation

- The comment describes the exercise; it does not run.
- `validate_user(username, password)` defines a function with two string parameters.
- `username == "admin"` tests the username. `password == "python123"` tests the password.
- `and` joins the comparisons, so both must be true for the returned value to be true.
- `main()` reads both values as strings. `input()` always returns text.
- The `if` calls `validate_user()`. A true result prints `Valid user`; false selects the `else` message.
- The entry guard calls `main()` only when this file runs directly.

### How it works

1. Ask for a username and a password.
2. Compare each input exactly with the required text.
3. Combine both comparisons with `and`.
4. Print the success or failure message.

### Example

Input:

```text
Enter username: admin
Enter password: python123
```

Expected output:

```text
Valid user
```

### Important concepts and limitations

- `==` compares values; `=` assigns a value to a variable.
- Matching is case-sensitive: `Admin` is different from `admin`.
- The password is visible while typed in a normal terminal.
- The username and password are written directly in source code. This is only suitable for a beginner exercise, not a real login system.

---

## 6. `discount.py`

### Program name and purpose

**Purchase discount calculator.** It selects a discount based on the purchase total and calculates how much remains to pay.

### What it does

Purchases of 5000 or more receive 20% off. Purchases from 3000 to below 5000 receive 10% off. Purchases below 3000 receive 5% off. The function returns both the discount and final payable amount.

### Code

```python
# Task 6: Apply a 20% discount for purchases >= Rs. 5000, 10% for
# Rs. 3000-4999, and 5% below Rs. 3000. Return discount and final amount.

def calculate_discount(purchase_amount):
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = round(purchase_amount * discount_rate, 2)
    final_amount = round(purchase_amount - discount_amount, 2)
    return discount_amount, final_amount


def main():
    try:
        purchase_amount = float(input("Enter the purchase amount in rupees: "))
        discount_amount, final_amount = calculate_discount(purchase_amount)
    except ValueError as error:
        print(error)
        return

    print(f"Discount amount: Rs. {discount_amount:.2f}")
    print(f"Final payable amount: Rs. {final_amount:.2f}")


if __name__ == "__main__":
    main()
```

### Line-by-line explanation

- `calculate_discount(purchase_amount)` takes the total as a parameter.
- If the amount is below zero, `raise ValueError(...)` creates an error and stops the function. Raising an error is how a function reports that it cannot continue with an invalid value.
- The `if`/`elif`/`else` block picks exactly one rate. It checks 5000 first, so 5000 does not accidentally receive the lower rate.
- `0.20`, `0.10`, and `0.05` mean 20%, 10%, and 5% as decimal multipliers.
- `purchase_amount * discount_rate` calculates the discount. `round(..., 2)` rounds it to two decimal places.
- Subtracting the discount gives the final amount.
- `return discount_amount, final_amount` returns two values. Python packages them as a tuple, which can be unpacked into two variables.
- `main()` reads a decimal amount and calls the function inside a `try` block.
- The `except ValueError as error` block catches either an invalid numeric input or the function's negative-amount error, then prints the error text.
- `:.2f` in each f-string displays exactly two digits after the decimal point.

### How it works

1. Enter a purchase amount.
2. Reject negative amounts.
3. Choose a discount rate based on the thresholds.
4. Calculate and round the discount and final amount.
5. Display both amounts with two decimal places.

### Example

Input:

```text
Enter the purchase amount in rupees: 4000
```

Expected output:

```text
Discount amount: Rs. 400.00
Final payable amount: Rs. 3600.00
```

### Important concepts and limitations

- `if`/`elif`/`else` selects one matching branch.
- A tuple can hold multiple returned values.
- Negative purchases are handled with `ValueError`.
- There is no upper limit for the amount and no currency symbol in the calculation; the program formats output with the text `Rs.`.

---

## 7. `access_control.py`

### Program name and purpose

**Access checker.** It decides whether a person can enter based on age, ID, or employee status.

### What it does

Access is granted when the person is at least 18 and has an ID, or when the person is an employee. Employee status is a separate way to qualify.

### Code

```python
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
```

### Line-by-line explanation

- `check_access(age, has_id, is_employee)` accepts an integer age and two Boolean values.
- `age >= 18 and has_id` is the first access route. Both parts must be true.
- `or is_employee` is the second route. If the person is an employee, the whole condition is true even if the first route is false.
- The function returns one of two strings.
- `read_yes_no(prompt)` is a helper function: a smaller function used by another function. It receives the prompt text as a parameter.
- `input(prompt)` displays the prompt and reads text. `.strip()` removes outside spaces and `.lower()` converts letters to lowercase.
- `answer not in ("yes", "no")` checks that only an accepted response was given. The parentheses create a tuple containing the two allowed answers.
- `raise ValueError(...)` reports an invalid answer. The function stops at that line.
- `return answer == "yes"` returns `True` for yes and `False` for no.
- In `main()`, `int()` converts age to a whole number. Each helper call returns a Boolean that is stored in a variable.
- The `try`/`except` catches invalid age text and invalid yes/no text. The final call passes all three arguments into `check_access()`.
- There is a whitespace-only line after the third input statement. It has no effect on the program.

### How it works

1. Read the age.
2. Ask the helper to read the ID answer and employee answer.
3. The helper validates each answer and converts it into a Boolean.
4. Apply the logical access condition.
5. Print the result, or print an input error.

### Example

Input:

```text
Enter age: 16
Do you have an ID? (yes/no): no
Are you an employee? (yes/no): yes
```

Expected output:

```text
Access granted
```

### Important concepts

- `and` requires both age and ID for the first route.
- `or` allows employee status to qualify independently.
- Parentheses make the condition grouping clear.
- A helper function avoids repeating yes/no conversion logic.
- Invalid responses are handled by raising and catching `ValueError`.

---

## 8. `skill_check.py`

### Program name and purpose

**Required-skill checker.** It checks whether a skill name is in a fixed list.

### What it does

The required list is `python`, `SQL`, `Git`, and `HTML`. The function returns a message saying whether the exact entered skill appears in the list.

### Code

```python
# Task 8: Check whether a skill is in ["python", "SQL", "Git", "HTML"]
# and report whether it is available.

REQUIRED_SKILLS = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in REQUIRED_SKILLS:
        return "Skill available"
    return "Skill not available"


def main():
    skill_name = input("Enter a skill name: ").strip()
    print(check_skill(skill_name))


if __name__ == "__main__":
    main()
```

### Line-by-line explanation

- `REQUIRED_SKILLS = [...]` creates a list. Square brackets are used for lists. The uppercase name is a common signal that this list is intended to remain fixed.
- `def check_skill(skill_name):` defines a function with one string parameter.
- `skill_name in REQUIRED_SKILLS` checks membership: does the exact value occur in the list?
- If found, the function returns `Skill available`. Otherwise, it returns `Skill not available`.
- `main()` reads a skill name. `.strip()` removes spaces from the start and end, but not spaces in the middle.
- `print(check_skill(skill_name))` calls the function and displays its returned message.
- The entry guard calls `main()` only when run directly.

### How it works

1. Python creates the required-skills list when it loads the file.
2. The user enters a name.
3. The program removes surrounding spaces.
4. The function checks the list with `in` and returns a message.
5. The message is printed.

### Example

Input:

```text
Enter a skill name: SQL
```

Expected output:

```text
Skill available
```

### Important concepts and limitations

- A list stores multiple values in order.
- `in` is the membership operator.
- String membership is case-sensitive: `SQL` is present, while `sql` is not.
- An empty input or an unlisted name is not an error; it returns `Skill not available`.

---

## 9. `operator_calculator.py`

### Program name and purpose

**Operator-based calculator.** It performs one selected arithmetic operation on two numbers.

### What it does

It supports `+`, `-`, `*`, `/`, `//`, `%`, and `**`. It reports an invalid operator with `ValueError` and prevents division-like operations from using zero as the second number.

### Code

```python
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
```

### Line-by-line explanation

- `calculate(a, operator, b)` receives a first number, an operator string, and a second number. The task itself uses the short parameter names `a` and `b`.
- Each `if operator == ...` compares the entered operator with one supported symbol. If it matches, the function performs that operation and returns immediately.
- `operator in ("/", "//", "%")` checks whether the operator is one of the three division-like operations. `and b == 0` checks whether the second number is zero too.
- If both checks are true, `raise ZeroDivisionError(...)` stops the calculation with a clear error.
- `a ** b` means a raised to the power b.
- If none of the supported operators matched, the final line raises `ValueError`.
- In `main()`, `float()` converts both number inputs and `.strip()` removes whitespace around the operator.
- The exception handler catches `ValueError` for bad number text or an unsupported operator, and `ZeroDivisionError` for division by zero. Both error types are displayed.

### How it works

1. Read the first number, operator, and second number.
2. Call `calculate()` with those three values.
3. The function selects an operation or raises an error.
4. Print the result or the caught error message.

### Example

Input:

```text
Enter the first number: 2
Enter an operator (+, -, *, /, //, %, **): **
Enter the second number: 3
```

Expected output:

```text
Result: 8.0
```

### Important concepts and limitations

- `ZeroDivisionError` is an error Python uses for division by zero.
- `ValueError` is used here when the chosen operator is not supported.
- `//` with floats can return a float-looking value, such as `2.0`.
- Python can also raise `ZeroDivisionError` for `0 ** -1`; the `main()` exception handler catches that error too.

---

## 10. `placement.py`

### Program name and purpose

**Placement eligibility and category checker.** It checks eligibility using marks, attendance, and backlog, then categorizes the candidate by experience.

### What it does

Placement eligibility is `Yes` when marks are at least 60, attendance is at least 75, and there is no backlog. Experience 0 is `fresher`, experience from 1 to 2 is `junior`, and other values reach the `experienced` branch. The result is returned in a dictionary.

### Code

```python
# Task 10: Accept age, marks, attendance, experience, and backlog status.
# Determine placement eligibility and classify experience as fresher,
# junior, or experienced.

def assess_placement(age, marks, attendance, experience, has_backlog):
    if experience == 0:
        category = "fresher"
    elif 1 <= experience <= 2:
        category = "junior"
    else:
        category = "experienced"

    eligible = marks >= 60 and attendance >= 75 and not has_backlog
    return {"placement_eligible": "Yes" if eligible else "No", "candidate_category": category}


def main():
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance: "))
    experience = float(input("Enter years of experience: "))
    has_backlog = input("Has backlog? (yes/no): ").lower() == "yes"
    result = assess_placement(age, marks, attendance, experience, has_backlog)
    print(f"Placement eligible: {result['placement_eligible']}")
    print(f"Candidate category: {result['candidate_category']}")


if __name__ == "__main__":
    main()
```

### Line-by-line explanation

- `assess_placement(...)` defines a function with five parameters. `age` is received, but it is not used in the function body.
- `if experience == 0:` sets the category to `fresher` when experience is exactly zero.
- `elif 1 <= experience <= 2:` is a chained comparison. It means experience is at least 1 and at most 2, including both endpoints.
- `else:` assigns `experienced` for every other value.
- `eligible = ...` checks marks, attendance, and backlog. The two `>=` comparisons check thresholds; `and` requires every requirement; `not` makes eligibility require no backlog.
- The returned dictionary contains two key/value pairs. The conditional expression chooses `Yes` or `No` for eligibility; the other value is the category.
- `main()` reads age as an integer and the other numeric values as floats.
- The backlog line lowercases the response and compares it with `yes`. The comparison itself produces `True` or `False`.
- The function call passes the five values in parameter order.
- The final two `print()` calls look up dictionary values by key and display them.
- The entry guard runs `main()` only when the file is started directly.

### How it works

1. Read age, marks, attendance, experience, and backlog response.
2. Convert numeric text to numbers and convert the backlog response to a Boolean.
3. Assign a category based on experience.
4. Check the three placement requirements.
5. Return both results in a dictionary and print them.

### Example

Input:

```text
Enter age: 22
Enter marks: 70
Enter attendance: 80
Enter years of experience: 1
Has backlog? (yes/no): no
```

Expected output:

```text
Placement eligible: Yes
Candidate category: junior
```

### Problems and edge cases in the actual code

- The `age` input is never used to decide eligibility. This matches the written condition, which has no age threshold, but means changing age alone cannot change the result.
- Negative experience is not rejected. It reaches the `else` branch and is labeled `experienced`, which may be unintended.
- Invalid numeric input is not inside a `try`/`except` block in this file. Typing letters for age, marks, attendance, or experience causes a `ValueError` traceback and stops the program.
- Backlog input is converted to lowercase but not stripped. `yes` works, but an answer with surrounding spaces such as ` yes ` becomes false and is treated as no backlog.
- The program does not validate whether marks or attendance are within 0 to 100.

---

# Quick Revision

These are the main Python ideas used by the programs in this folder.

- **Variables:** Names such as `marks`, `attendance`, and `final_amount` hold values so the program can use them later.
- **Data types:** `int` is a whole number; `float` can contain decimals; `str` is text; `bool` is either `True` or `False`.
- **Input and output:** `input()` reads text from the user. `print()` displays information. Convert input text with `int()` or `float()` before doing numeric comparisons or math.
- **Arithmetic operators:** `+`, `-`, `*`, `/`, `//`, `%`, and `**` perform addition, subtraction, multiplication, division, floor division, remainder, and exponentiation.
- **Comparison operators:** `==`, `>=`, and related operators compare values and return a Boolean.
- **Logical operators:** `and` requires all joined conditions to be true; `or` requires at least one; `not` reverses true/false.
- **Membership:** `in` and `not in` check whether a value is in a list or tuple.
- **`if`/`elif`/`else`:** These choose which indented code should run based on conditions.
- **Loops:** `for` repeats code for each item. `calculator.py` uses a `for` loop to print each calculator result. The other files do not use loops.
- **Functions:** `def` defines reusable code. Calling a function runs it.
- **Parameters and arguments:** Parameters are names in the function definition; arguments are the actual values passed in a call.
- **`return`:** Sends a result back to the caller and ends that function. It is different from `print()`, which only displays text.
- **Built-in functions:** The files use `input()`, `print()`, `float()`, `int()`, `round()`, and `ValueError`/`ZeroDivisionError` exception types.
- **Lists:** `REQUIRED_SKILLS` is a list of strings in `skill_check.py`.
- **Tuples:** `discount.py` returns two values as a tuple. `student_eligibility.py` and `access_control.py` also use tuples to list allowed text responses.
- **Dictionaries:** Several functions return dictionaries so results can be named and retrieved by keys, for example `result["candidate_category"]`.
- **Strings:** Text values use quotes. `.strip()` removes outside spaces; `.lower()` converts letters to lowercase; f-strings insert values inside `{}`.
- **Conditional expressions:** The form `value_if_true if condition else value_if_false` chooses between two values. It is used in `number_check.py` and `placement.py`.
- **Exception handling:** `try` begins a block that might fail; `except` handles a named error. `raise` creates an error deliberately. These are used in most programs to handle invalid input; `placement.py` does not handle conversion errors.
- **Modules and imports:** The files do not import other modules. The `if __name__ == "__main__":` pattern checks whether each file was run directly before calling `main()`.
- **Sets:** No set is used in these files.
- **Identity operators:** `is` and `is not` do not appear in these files.

A simple way to trace any program is: identify the inputs, follow each condition, note the calculation, check what the function returns, and then see what `main()` prints.
