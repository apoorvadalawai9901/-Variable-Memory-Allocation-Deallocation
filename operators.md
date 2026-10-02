python has below operators
1. Airthametric operators
2. Assignment operators
3. comparision operators
4. Logical operators
5. identity operators
6. membership operators
7. Bitwise operators
8. ternary operators

Task 1:
File: calculator.py
   write calculator program which should return addition substraction multiplication,devision,floor division,reaminder

Task 2:
File: number_check.py
    create function that accepts an integer and determines
    * whether the number is even or odd
    * whether it is divisible by 3
    *  whether it is divisiblle by 5 
Task 3:
File: marks_result.py
    create a function that accepts a students marks and returns 
    * pass if marks are >=35 
    *fail otherwise
    * distinction if marks>=75
    
Task 4:
File: student_eligibility.py
    create a function that accepts 
    *marks
    *attebdence percentage
    *backlog status
     a student is eligilbe only when marks>=60 and attendence >=75 and backlog==false
     return eligible or not eligible 

Task 5:
File: user_validation.py
    create a function that accepts user name and passowrd. 
    the user should be considered valid only when 
    username=="admin" and password=="python123"

Task 6: 
File: discount.py
    create a function taht accepts the purchaes amount
    apply
     rupees 5000 or more(20% dis)
    if  rupees3000 to 4999 (10%disc)
     below rupees 3000 (5% disc)
     return discount amount and final payable amount

Task 7:
File: access_control.py
    create a function that accepts age,has_id,is_employee
    allow access when age>=18 and has_id==true
    or whenis_employee==true
    return access granted or access deniged

Task 8:
File: skill_check.py
create a list of requrieed skills 
["python","SQL","Git","HTML"]
create a function that accepts skill name and checks whether it exits in the list
display skill available or skil or not available 

Task 9:
File: operator_calculator.py
     create 
     calculate(a ,opetaor,b):
      the function should support (+,-,*,/,//,% and **)
      handle invalid operators and division by zero

    Task 10:
File: placement.py
      create function that accepts 
      age, marks,attendence,experience,has_backlog
       determine palacement eligilbilty 
       marks>=60 and attendence>=75 has_backlog==false
       than determine a category
       expereience==0->fresher
       experience 1 to 2->junior
       expereince >2->experinced
       finally display
       placement eligible "yes"/"no"
       candidate category :fresher or junior or experinced

---

## Operator explanations and task walkthroughs

An operator tells Python to perform an action on one or more values. For example, `5 + 2` uses the `+` operator to add two values. The tasks above use arithmetic, comparison, logical, and membership operators most often.

### The main operator categories

#### 1. Arithmetic operators

Arithmetic operators perform calculations:

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Addition | `5 + 2` gives `7` |
| `-` | Subtraction | `5 - 2` gives `3` |
| `*` | Multiplication | `5 * 2` gives `10` |
| `/` | Division | `5 / 2` gives `2.5` |
| `//` | Floor division | `5 // 2` gives `2` |
| `%` | Remainder | `5 % 2` gives `1` |
| `**` | Exponentiation | `5 ** 2` gives `25` |

#### 2. Assignment operators

Assignment operators store or update a value in a variable. `=` assigns a value, as in `marks = 80`. Compound assignment combines an operation with assignment: `total += 5` means `total = total + 5`.

#### 3. Comparison operators

Comparison operators compare values and produce `True` or `False`. Common examples are `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater than or equal), and `<=` (less than or equal). For example, `marks >= 60` is true when marks are 60 or higher.

#### 4. Logical operators

Logical operators combine or reverse Boolean conditions. `and` requires both sides to be true; `or` requires at least one side to be true; `not` reverses a Boolean. For example, `marks >= 60 and attendance >= 75` is true only when both minimums are met.

#### 5. Identity operators

`is` and `is not` check whether two names refer to the same object. They are different from `==`, which checks whether values are equal. Use `==` for ordinary comparisons such as username or number checks. Identity checks are most commonly useful for values such as `None` (`value is None`).

#### 6. Membership operators

`in` checks whether a value exists in a collection; `not in` checks that it does not. For example, `"SQL" in ["python", "SQL"]` is true. Membership also works with strings, lists, tuples, sets, and dictionary keys.

#### 7. Bitwise operators

Bitwise operators act on the binary bits of integers. Examples include `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), and `>>` (right shift). They are useful for low-level flags and binary data, but none of the ten tasks needs them.

#### 8. Conditional expression (ternary expression)

A conditional expression chooses one of two values in a single expression: `"Even" if number % 2 == 0 else "Odd"`. It is sometimes called a ternary expression because it has a condition and two possible values. The task programs mostly use regular `if` statements because those are easier to read when there are several conditions.

### How operators are used in each task

#### Task 1: `calculator.py`

The calculator applies `+`, `-`, `*`, `/`, `//`, and `%` to the two input numbers. `/` may return a fractional value; `//` returns the quotient rounded down; `%` returns the remainder. Since division, floor division, and remainder need a nonzero second number, the function checks `second_number == 0` before calculating them. The `+` inside the returned dictionary is a dictionary-unpacking operation (`**division_results`), not exponentiation.

#### Task 2: `number_check.py`

The modulo operator `%` finds remainders. The comparison `number % 2 == 0` checks whether a number is even. Similarly, remainders of zero for `% 3` and `% 5` indicate divisibility by those numbers. Each `== 0` comparison returns a Boolean value for the result dictionary.

#### Task 3: `marks_result.py`

The comparisons `marks >= 75` and `marks >= 35` test the grade thresholds. The function checks the distinction condition first, then the pass condition. `if` and `return` choose one result and stop the function once that result is known.

#### Task 4: `student_eligibility.py`

The comparisons `marks >= 60` and `attendance >= 75` check the numeric requirements. The `not` operator makes `not has_backlog` true only when the backlog flag is false. The `and` operator combines all three conditions, so failing any one condition makes the student ineligible.

#### Task 5: `user_validation.py`

The `==` operator compares the username with `"admin"` and the password with `"python123"`. The `and` operator requires both comparisons to match. The function returns the resulting Boolean; `main()` uses it in an `if` statement to print a message.

#### Task 6: `discount.py`

The comparisons `purchase_amount >= 5000` and `purchase_amount >= 3000` select the discount tier. The `if`/`elif` order matters: the highest threshold must be tested first. Multiplication (`*`) computes the discount, and subtraction (`-`) computes the amount due after discount.

#### Task 7: `access_control.py`

The comparison `age >= 18` checks the age rule. The expression `(age >= 18 and has_id) or is_employee` requires both adult age and ID for the first path, but employee status alone satisfies the second path. Parentheses make the intended grouping explicit.

#### Task 8: `skill_check.py`

The membership operator `in` checks whether `skill_name` is in `REQUIRED_SKILLS`. If present, the function returns `"Skill available"`; otherwise it returns `"Skill not available"`. String membership is case-sensitive, so `"SQL"` and `"sql"` are different values.

#### Task 9: `operator_calculator.py`

The `operator` parameter is compared with each supported symbol using `==`. The matching branch performs its arithmetic operation. The expression `operator in ("/", "//", "%")` uses membership to identify operations that cannot use a zero divisor. If no operator matches, the function raises `ValueError`.

#### Task 10: `placement.py`

The comparisons `marks >= 60` and `attendance >= 75` test the academic thresholds. `not has_backlog` requires the backlog flag to be false, and `and` requires all three conditions. A separate `if`/`elif` chain compares experience with zero and the range from 1 through 2 to choose the category. Age is accepted but is not checked because the task does not specify an age condition.

### `print()` and `return` are different

The functions in the task files usually `return` a result. Returning gives that value back to the caller so it can be stored, tested, or used in another calculation. `print()` displays a value on the screen. The `main()` function generally handles printing, while the reusable task function handles the decision or calculation.

---

## Code-wise operator examples

The comments below explain the key operator expressions used in each task. They are shortened examples of the expressions in the Python files.

### Task 1: Arithmetic

```python
sum_result = first_number + second_number      # Add the two numbers.
quotient = first_number / second_number        # Divide; result may contain decimals.
whole_quotient = first_number // second_number  # Divide and round down.
remainder = first_number % second_number       # Keep the remainder after division.
```

The actual calculator also uses `-` for subtraction and `*` for multiplication. It checks `second_number == 0` before the last three division-based operations.

### Task 2: Divisibility

```python
is_even = number % 2 == 0          # True when division by 2 leaves no remainder.
divisible_by_3 = number % 3 == 0   # True when division by 3 leaves no remainder.
divisible_by_5 = number % 5 == 0   # True when division by 5 leaves no remainder.
```

`%` calculates a remainder, and `== 0` compares it with zero. The comparison returns a Boolean value.

### Task 3: Marks conditions

```python
if marks >= 75:       # Comparison checks the distinction threshold.
    result = "Distinction"
elif marks >= 35:     # Checked only if marks were below 75.
    result = "Pass"
else:
    result = "Fail"  # Used when both comparisons are false.
```

`>=` includes the threshold itself. The `if`/`elif` order ensures distinction takes precedence over pass.

### Task 4: Logical AND and NOT

```python
eligible = marks >= 60 and attendance >= 75 and not has_backlog
# and requires all conditions; not has_backlog requires a False backlog flag.
```

If any of the three checks is false, `eligible` becomes false.

### Task 5: Equality and AND

```python
valid = username == "admin" and password == "python123"
# == compares each value; and requires both comparisons to be true.
```

The string comparisons are exact and case-sensitive.

### Task 6: Discount tiers

```python
if amount >= 5000:       # Compare with the highest tier first.
    rate = 0.20
elif amount >= 3000:     # Reached only for amounts below 5000.
    rate = 0.10
else:
    rate = 0.05           # Remaining nonnegative amounts are below 3000.

discount = amount * rate  # Multiplication calculates the discount.
payable = amount - discount  # Subtraction calculates the final price.
```

### Task 7: Logical AND and OR

```python
allowed = (age >= 18 and has_id) or is_employee
# Both age and ID are required for the first route; employee status is another route.
```

Parentheses group the first route. `or` grants access if that route succeeds or the person is an employee.

### Task 8: Membership

```python
skill_available = skill_name in REQUIRED_SKILLS
# in checks whether the exact skill string is present in the list.
```

For example, `"SQL" in REQUIRED_SKILLS` is true, but `"sql" in REQUIRED_SKILLS` is false because capitalization differs.

### Task 9: Operator selection and zero checking

```python
if operator == "+":        # == checks which operator the user selected.
    result = a + b
elif operator == "**":     # ** means exponentiation in this expression.
    result = a ** b
elif operator in ("/", "//", "%") and b == 0:
    raise ZeroDivisionError("Cannot divide by zero")
```

The `in` expression checks whether the selected operator is one of the division-based operators. In the full function, each supported operator has its own branch and unsupported operators raise `ValueError`.

### Task 10: Eligibility and category

```python
eligible = marks >= 60 and attendance >= 75 and not has_backlog
# All placement requirements must pass.

if experience == 0:          # == checks for exactly zero years.
    category = "fresher"
elif 1 <= experience <= 2:   # Chained comparisons include both endpoints.
    category = "junior"
else:
    category = "experienced"
```

Eligibility and experience category are separate decisions: a candidate can be in a category even when placement eligibility is `No`.
