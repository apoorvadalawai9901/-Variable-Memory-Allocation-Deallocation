# Functions in Python

## 1. Why do we need functions?

Functions are one of the most important concepts in Python because they help us write cleaner and more efficient programs.

Consider the following example:

```python
print("Apoorva")
print("Sandhya")
print("Spoorti")
```

This works, but it repeats the same code three times. If we want to print the name of many people, the program becomes long and difficult to maintain.

Now look at the function version:

```python
def welcome(name):
    print("Welcome", name)

welcome("Apoorva")
welcome("Sandhya")
welcome("Spoorti")
```

This is better because the same logic is written once and reused many times.

### Benefits of functions

- Code reuse: write once, use many times
- Less repetition: avoid duplicating the same logic
- Better organization: group related logic together
- Easier maintenance: fix a bug in one place
- Easier testing: test small blocks of code separately

---

## 2. What is a function?

A function is a reusable block of code that performs a specific task.

A function may:

- take inputs
- process them
- return a result

Example:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

This function takes two values, adds them, and returns the answer.

---

## 3. Defining vs calling a function

### Defining a function

A function is defined using the `def` keyword:

```python
def greet():
    print("Hello")
```

This only creates the function. It does not run the code inside it yet.

### Calling a function

To execute the function, we call it:

```python
def greet():
    print("Hello")

greet()
```

Output:

```python
Hello
```

The important difference is:

- Defining a function creates the blueprint
- Calling a function actually runs it

---

## 4. Functions without parameters

A function may not require any input values.

```python
def welcome():
    print("Welcome to Nighan2 Labs")

welcome()
```

This is the simplest form of a function. It performs a task without receiving any data.

---

## 5. Functions with parameters

Parameters are variables used in the function definition.

```python
def welcome(name):
    print("Welcome", name)

welcome("Apoorva")
```

Here:

- `name` is the parameter
- `"Apoorva"` is the argument passed to the function

A parameter is a placeholder used inside the function, while an argument is the actual value supplied when the function is called.

---

## 6. Functions with multiple parameters

A function can accept more than one parameter.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This prints:

```python
30
```

Functions can take any number of parameters depending on the task.

---

## 7. The `return` statement

The `return` statement is one of the most important parts of a function.

### Without `return`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This prints the result, but the result is not sent back to the caller.

### With `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```python
30
```

### Key idea

- `print()` displays a value on the screen
- `return` sends a value back to the caller

So `print()` is for output, while `return` is for sending data to the rest of the program.

---

## 8. What happens after `return`?

Once a `return` statement is executed, the function exits immediately.

```python
def test():
    return 10
    print("Hello")

print(test())
```

The line `print("Hello")` will never execute because control leaves the function as soon as `return` is reached.

This is a very important concept in Python programming.

---

## 9. Returning multiple values

Python allows a function to return more than one value.

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)
print(y)
print(z)
```

Output:

```python
15
5
50
```

This function effectively returns a tuple of values.

---

## 10. Default parameters

A default parameter gives a value to a parameter if the caller does not pass one.

```python
def greet(name="Apoorva"):
    print("Hello", name)

greet()
greet("Sandhya")
```

Output:

```python
Hello Apoorva
Hello Sandhya
```

### Why use default parameters?

They are useful when a parameter is optional. For example, if a function usually uses a common value, we can define it as a default instead of forcing the caller to provide it every time.

---

## 11. Positional arguments

When arguments are passed in the same order as the parameters, they are called positional arguments.

```python
def student(name, age):
    print(name, age)

student("Apoorva", 21)
```

The first value goes to `name`, and the second goes to `age`.

---

## 12. Keyword arguments

Keyword arguments are passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=21, name="Apoorva")
```

Here, the order does not matter because we explicitly mention the names.

---

## 13. Positional and keyword arguments together

A function can accept both positional and keyword arguments, but the order matters.

```python
def student(name, age, course):
    print(name, age, course)

student("Apoorva", 21, course="BCA")
```

This is valid.

But the following is invalid:

```python
def student(name, age, course):
    print(name, age, course)

student(name="Apoorva", age=21, "BCA")
```

This will raise an error because a positional argument cannot be placed after a keyword argument.

A correct version is:

```python
def student(name, age, course):
    print(name, age, course)

student("Apoorva", 21, "BCA")
```

---

## 14. `*args` - variable number of positional arguments

The `*args` syntax allows a function to accept any number of positional arguments.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

Output:

```python
30
60
15
```

### Explanation

`*numbers` collects all positional arguments into a tuple. This makes the function flexible and useful when the number of inputs is not fixed.

---

## 15. `**kwargs` - variable number of keyword arguments

The `**kwargs` syntax allows a function to accept any number of keyword arguments.

```python
def student(**details):
    print(details)

student(name="Apoorva", age=21, course="BCA")
```

Output:

```python
{'name': 'Apoorva', 'age': 21, 'course': 'BCA'}
```

### Explanation

`**details` collects all keyword arguments into a dictionary-like structure.

---

## 16. Combining positional arguments, default values, `*args`, and `**kwargs`

A function can combine several types of parameters:

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

example(1, 2, 3, 4, 5, name="Apoorva", age=21)
```

### Explanation

- `a` is a required positional argument
- `b` is an optional positional argument with a default value
- `*args` collects extra positional values
- `**kwargs` collects extra keyword arguments

This pattern is very powerful when designing flexible APIs.

---

## 17. Scope: local vs global variables

Variable scope refers to where a variable can be used.

### Local variables

```python
def test():
    x = 10
    print(x)

test()
```

Here, `x` is a local variable. It exists only inside the function.

### Global variables

```python
x = 100

def test():
    print(x)

test()
```

Here, `x` is a global variable. The function can read it.

### Important point

- Local variables are available only inside the function
- Global variables are available throughout the program

---

## 18. The `global` keyword

If we want to modify a global variable from inside a function, we must use the `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

Output:

```python
1
```

### Best practice

Using `global` is not always recommended. It can make programs harder to understand and debug.

A better design is usually:

- pass values as parameters
- return results
- keep state local when possible

---

## 19. Local scope inside function

```python
def test():
    x = 10

test()
print(x)
```

This raises a `NameError` because `x` is local to `test()` and cannot be accessed outside the function.

This is an example of how local scope works in Python.

---

## 20. Functions can call other functions

A function can use another function as part of its work.

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

Output:

```python
30
```

This shows that functions can work together in a program.

### Flow of execution example

```python
main() -> validate() -> save() -> display()
```

This means one function may call another, which may call another, and so on. This is a common structure in larger programs.

---

## 21. Summary

Functions are essential in Python because they:

- reduce repetition
- improve readability
- help organize code
- make code reusable
- support modular programming

A function may:

- take no arguments
- take one or more arguments
- return a value
- return multiple values
- use default values
- accept variable numbers of arguments

In short, functions make programs more structured, efficient, and maintainable.

---

## 22. Quick revision examples

### Example 1: Basic function

```python
def greet():
    print("Hello")

greet()
```

### Example 2: Function with parameter

```python
def greet(name):
    print("Hello", name)

greet("Apoorva")
```

### Example 3: Function with return value

```python
def square(n):
    return n * n

print(square(5))
```

### Example 4: Default parameter

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
```

### Example 5: `*args`

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
```

### Example 6: `**kwargs`

```python
def show(**details):
    print(details)

show(name="Apoorva", age=21)
```

---

## 23. Final thought

Understanding functions is a major step in learning Python. Once you are comfortable with them, you can build larger and more advanced programs with much less confusion. Functions are not just a coding trick - they are the foundation of good programming structure.

## 24. Function calling flow

When a function is called, Python transfers control to it, passes the arguments, runs its statements, and returns control to the calling line.

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)
```

The function receives `5` and `4`, calculates their product, returns `20`, and stores it in `result`.

---

## 25. Functions are objects

In Python, a function is an object. It can be stored in another variable and called through that variable.

```python
def greet():
    print("Hello world")

x = greet
x()
```

`greet` refers to the function, while `greet()` calls it.

---

## 26. Passing a function to another function

Functions can be passed as arguments to other functions.

```python
def square(value):
    return value * value

def process(function, value):
    return function(value)

print(process(square, 5))
```

Output: `25`

---

## 27. Higher-order functions

A higher-order function accepts another function as an argument or returns a function as its result. The `process()` function above is a higher-order function.

---

## 28. Lambda functions

A lambda is a small anonymous function written in a single expression.

```python
square = lambda value: value * value
print(square(5))

numbers = [1, 2, 3, 4]
result = list(map(lambda value: value * 2, numbers))
print(result)
```

---

## 29. Recursion

Recursion is a technique in which a function calls itself. A recursive function needs a base case so that the calls eventually stop.

```python
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)
```

The condition `number == 0` is the base case.

---

## 30. Function documentation

A docstring documents what a function does.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)
```

---

## 31. Type hints

Type hints communicate the expected types of parameters and return values. Python generally does not enforce them automatically at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## 32. A practical program: electricity bill

Functions separate the calculation from the input and output parts of a program.

```python
def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 4
    else:
        amount = 100 * 2 + 100 * 4 + (units - 200) * 6
    return amount + 100

units = int(input("Enter units: "))
bill = calculate_bill(units)
print("Bill:", bill)
```

Functions provide separation of responsibility, reusability, easier testing, better readability, and easier maintenance.

---

## 33. Function design

A good function generally has input, processing, and output. Each function should have a clear purpose and a meaningful name.

---

## 34. Do not create giant functions

A large function that handles every part of a system is difficult to read, test, and maintain. Separate responsibilities into smaller functions:

```python
def get_student():
    pass

def validate_student(student):
    pass

def calculate_student(student):
    pass

def save_student(student):
    pass

def display_student(student):
    pass
```

This follows the single responsibility principle: each function should focus on one main task.