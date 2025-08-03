# Python Crash Course for Beginners - Notes_1

## 1. What is a Programming Language? (Python)
- A **programming language** is a way to give instructions to a computer to perform tasks.
- **Python** is a high-level, easy-to-learn programming language known for its simplicity and readability.
- Used for web development, data analysis, AI, automation, and more.
- Python is beginner-friendly due to its clear syntax, like writing in plain English.

## 2. Writing a Simple String Print Statement
- Use the `print()` function to display text or data in the terminal.
- Example: Printing your name.

```python
print("Danish")
```
- **Explanation**: The text inside quotes (`"Danish"`) is a **string**. The `print()` function outputs it to the terminal.

## 3. External Modules in Python
- Python has built-in functions, but you can add more features using **external modules**.
- Install modules using `pip`, Python's package manager, in the terminal.
- Examples:
  - **Flask**: A module for building web applications.
    ```bash
    pip install flask
    ```
  - **Pyjokes**: A fun module to generate random programming jokes.
    ```bash
    pip install pyjokes
    ```
- After installation, import the module in your Python code to use it.

## 4. Using Python as a Calculator in the Terminal
- Python can perform calculations directly in the terminal (or Python shell).
- Open the terminal, type `python` or `python3`, and press Enter to start the Python interpreter.
- Examples:
  - Addition: `5 + 3` outputs `8`
  - Multiplication: `5 * 10` outputs `50`
  - Division: `10 / 2` outputs `5.0`
- No need to write a full program—just type math expressions and press Enter!

## 5. Comments in Python
- **Comments** are notes in code that Python ignores, used to explain what the code does.
- **Single-line comment**: Starts with `#`.
  ```python
  # This is a single-line comment
  print("Hello")  # Prints Hello
  ```
- **Multi-line comment**: Use triple quotes (`'''` or `"""`) for multiple lines.
  ```python
  '''
  This is a multi-line comment.
  It can span multiple lines.
  Useful for detailed explanations.
  '''
  print("World")
  ```

## Practice Section
### Q1. Write a Python program to print a full paragraph
- Create a program that prints a short paragraph about yourself.

```python
print("Hi, I am Danish. I run a YouTube channel called Ai_Code_With_Danish. This is my first video in the Python Crash Course for Beginners. I love teaching coding in a fun and simple way!")
```

### Q2. Multiply 5 to 10 one by one in the terminal
- Open the Python terminal (type `python` or `python3`).
- Type the following commands one by one:
  ```python
  5 * 1  # Outputs: 5
  5 * 2  # Outputs: 10
  5 * 3  # Outputs: 15
  5 * 4  # Outputs: 20
  5 * 5  # Outputs: 25
  5 * 6  # Outputs: 30
  5 * 7  # Outputs: 35
  5 * 8  # Outputs: 40
  5 * 9  # Outputs: 45
  5 * 10  # Outputs: 50
  ```
- **Tip**: You can write a loop in a program to automate this (shown later in the course).

### Q3. Python Program Using pyttsx3 Library
- Task: Create a text-to-speech program that says, "Hi, I am Danish. Tell me about yourself."
- **Note**: You need to install `pyttsx3` first: `pip install pyttsx3`.

```python
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the sentence to speak
sentence = "Hi, I am Danish. Tell me about yourself."

# Speak the sentence
engine.say(sentence)

# Process the speech
engine.runAndWait()
```

### Q4. Python Program to List Directory Contents
- Task: Use the `os` module to list all items in a folder.

```python
import os

# Define the directory path
directory_path = '/New folder/'  # Replace with your folder path

# Get all items in the directory
items = os.listdir(directory_path)

# Loop through and print each item
for item in items:
    print(item)
```
