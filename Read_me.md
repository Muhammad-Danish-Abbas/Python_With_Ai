# Python Crash Course for Beginners - Chapter_2_Notes

## 1. Variables in Python
Variables are like containers that store data in your program. You can assign values to variables and use them later. For example:

```python
a = 2
b = 8
print(a + b)  # Outputs: 10
name = "Danish"
print(name)  # Outputs: Danish
print(a + b)  # Outputs: 10 again
```

**Explanation:**
- `a = 2` assigns the value `2` to the variable `a`.
- `b = 8` assigns the value `8` to the variable `b`.
- `print(a + b)` adds the values of `a` and `b` and prints the result.
- `name = "Danish"` assigns the string `"Danish"` to the variable `name`.
- You can reuse variables in multiple `print()` statements.

## 2. Data Types in Python
Python supports different types of data that variables can hold. Here are common data types:

```python
a = 2           # Integer: Whole numbers
b = 3.5         # Float: Decimal numbers
c = "Danish"    # String: Text or characters
d = False       # Boolean: True or False
e = None        # None: Represents no value
```

**Explanation:**
- **Integer**: Whole numbers like `2`, `10`, or `-5`.
- **Float**: Numbers with decimals like `3.5`, `0.1`, or `-2.7`.
- **String**: Text enclosed in quotes (`""` or `''`), like `"Danish"`.
- **Boolean**: Either `True` or `False`, used for conditions.
- **None**: A special type representing no value or empty.

## 3. Rules for Defining Variable Names
When naming variables in Python, follow these rules:
- Variable names can contain letters (`a-z`, `A-Z`), numbers (`0-9`), and underscores (`_`).
- Names **cannot start** with a number. Example: `1name` is invalid, but `name1` is valid.
- Names are case-sensitive: `name` and `Name` are different variables.
- Avoid using Python keywords (like `print`, `for`, `if`) as variable names.
- Use descriptive names for clarity, e.g., `age` instead of `a`.
- Example of valid names: `user_name`, `total_score`, `my_age`.
- Example of invalid names: `2age`, `user-name`, `for`.

## 4. Practice Section
Try these beginner-friendly practice questions to reinforce your learning!

### Q1. Create a program to store and print your favorite number and food
Write a program that:
- Creates a variable for your favorite number.
- Creates a variable for your favorite food.
- Prints both variables.

```python
favorite_number = 7
favorite_food = "Pizza"
print("My favorite number is:", favorite_number)
print("My favorite food is:", favorite_food)
```

### Q2. Calculate the area of a rectangle
Write a program that:
- Creates variables for the length and width of a rectangle.
- Calculates the area (length × width).
- Prints the area.

```python
length = 10
width = 5
area = length * width
print("The area of the rectangle is:", area)
```

### Q3. Swap two variables
Write a program that:
- Creates two variables, `x` and `y`, with values `10` and `20`.
- Swaps their values (so `x` becomes `20` and `y` becomes `10`).
- Prints the new values.

```python
x = 10
y = 20
temp = x    # Store x in a temporary variable
x = y       # Assign y's value to x
y = temp    # Assign temp (original x) to y
print("x is now:", x)
print("y is now:", y)
```

### Q4. Combine strings and numbers
Write a program that:
- Creates a variable for your name (string).
- Creates a variable for your age (integer).
- Prints a sentence combining both, like "My name is Danish and I am 25 years old."

```python
name = "Danish"
age = 20
print("My name is", name, "and I am", age, "years old.")
```