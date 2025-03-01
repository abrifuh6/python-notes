# Python Notes

## Table of Contents


1. [Introduction](#introduction)
    - [Syntax](#1-syntax)
    - [Semantics](#2-semantics)

2. [ABCs Of Python](#abcs-of-python)
    - [Variables](#-variables)
        - [Variable Naming Conventions in Python](#variable-naming-conventions-in-python)
    - [Operators](#-operators)
    - [Conditions](#-conditions)
    - [Loops](#-loops)
        - [for Loop](#i-for-loop)
        - [while Loop](#ii-while-loop)
        - [Nested Conditions](#iv-nested-conditions)
    - [Numbers](#-numbers)
        - [Integers](#i-integers)
        - [Floating-Point Numbers](#ii-floating-point-numbers)
        - [Complex Numbers](#iii-complex-numbers)
    - [Strings](#-strings)
        - [String Basics](#1-string-basics)
        - [String Concatenation](#ii-string-concatenation)
        - [String Indexing and Slicing](#iii-string-indexing-and-slicing)
        - [String Methods](#string-methods)
    - [Lists](#-lists)
        - [List Basics](#i-list-basics)
        - [Accessing Elements in a List](#i-accessing-elements-in-a-list)
    - [Tuples](#-tuples)
    - [Dictionary](#-dictionary)
        - [Creating Dictionaries](#creating-dictionaries)
        - [Accessing and Modifying Dictionaries](#accessing-and-modifying-dictionaries)
        - [Dictionary Functions](#dictionary-functions)
    - [DateTime()](#-datetime)
    - [Functions](#-functions)
        - [Function Definition](#how-does-on-define-functions)
        - [Functions with Multiple Parameters](#functions-with-multiple-parameters)
    - [Modules](#-modules)
        - [Importing Modules](#importing-modules)
        - [Using Standard Library Modules](#using-standard-library-modules)
        - [Creating Your Own Modules](#creating-your-own-modules)
        - [Module Aliasing](#module-aliasing)
    - [Exceptions](#-exceptions)
        - [Handling Exceptions](#handling-exceptions)
        - [Raising Exceptions](#raising-exceptions)
        - [Custom Exceptions](#custom-exceptions)
        - [Exception Handling Best Practices](#exception-handling-best-practices)

## Introduction

Every programing language has 2 things.

- **Syntax**
- **Semantics**

## 1. Syntax

**Syntax** refers to the set of rules that dictate how you must write your code so that the computer can understand and execute it correctly. It's like the grammar rules in a language. Following the correct syntax is crucial because even small mistakes can prevent the computer from understanding your instructions.

 It's a bit like making sure you use the right words and punctuation when writing a sentence so that others can understand what you're saying.

 ## 2. **Semantics**

In programming, **semantics** refers to the meaning or intended behavior of your code. It's not just about following the correct syntax (grammar rules), but also ensuring that your instructions make sense and do what you want them to do. It's like using the right words in a sentence and arranging them properly so that your message is clear and achieves the desired outcome. If syntax is about the structure of your code, semantics is about its meaning and functionality.


## ABCs Of Python

## - Variables

Variables are reserved memory locations to store values. 

In Python, a variable is like a container that holds information. It's a way to give a name to a piece of data so that you can use it later. Think of it as a label you put on a box to help you remember what's inside.

For example, if you want to remember someone's age, you might create a variable called `age`:

```xyz.py
age = 25
```

Now, whenever you use the word **"age"** in your program, Python knows you're talking about the number **25**.

## Variable Naming Conventions in Python

When naming variables in Python, it's important to follow certain conventions to enhance code readability. Here are the common variable naming conventions:

1. **Snake Case:**
   - Use lowercase letters with underscores to separate words.
   - Example: `my_variable`, `user_age`, `total_count`

2. **Camel Case:**
   - Start with a lowercase letter and capitalize the first letter of each subsequent concatenated word.
   - Example: `myVariable`, `userAge`, `totalCount`

3. **Descriptive Names:**
   - Choose names that are descriptive and convey the purpose of the variable.
   - Examples:
     ```python
     # Good
     total_count = 42
     user_name = "John"

     # Avoid
     x = 42
     y = "John"
     ```

4. **Avoid Single-Character Names (Except in Certain Cases):**
   - Use single-character names only for simple loop counters or in contexts where the meaning is clear.
   - Example:
     ```python
     # Good
     for i in range(10):
         print(i)

     # Avoid
     a = 10
     ```

5. **Avoid Reserved Keywords:**
   - Do not use Python reserved keywords for variable names.
   - Example:
     ```python
     # Avoid
     class = "Python"
     ```

6. **Use Uppercase for Constants:**
   - If you have constants, use uppercase letters with underscores.
   - Example:
     ```python
     MAX_VALUE = 100
     PI = 3.14
     ```

7. **Be Consistent:**
   - Maintain consistency in naming across your codebase. If you start with one convention, stick to it.

   - Remember that these conventions contribute to code readability and collaboration. Following a consistent naming style makes it easier for you and others to understand and maintain the code.

## - Operators

In Python, operators are symbols that perform operations on variables and values. Here are the main types of operators:

## 1. Arithmetic Operators

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `%`: Modulus (remainder)
- `**`: Exponentiation

## 2. Comparison Operators

- `==`: Equal to
- `!=`: Not equal to
- `<`: Less than
- `>`: Greater than
- `<=`: Less than or equal to
- `>=`: Greater than or equal to

## 3. Logical Operators

- `and`: Logical AND
- `or`: Logical OR
- `not`: Logical NOT

## 4. Assignment Operators

- `=`: Assign
- `+=`: Add and assign
- `-=`: Subtract and assign
- `*=`: Multiply and assign
- `/=`: Divide and assign
- `%=`: Modulus and assign

## 5. Bitwise Operators

- `&`: Bitwise AND
- `|`: Bitwise OR
- `^`: Bitwise XOR
- `~`: Bitwise NOT
- `<<`: Left shift
- `>>`: Right shift

## 6. Membership Operators

- `in`: True if value is found in the sequence
- `not in`: True if value is not found in the sequence

## 7. Identity Operators

- `is`: True if both variables reference the same object
- `is not`: True if variables reference different objects

These operators allow you to perform a wide range of operations in Python, enabling you to manipulate and compare values in your code.

## - Conditions

In Python, conditions are like decision points that determine the flow of your program. They allow you to execute different blocks of code based on whether certain conditions are true or false.

### i. `if` Statement

The `if` statement is the simplest form of a condition. It checks whether a specified condition is true and, if so, executes a block of code.

```python
if condition:
# Code to execute if the condition is true.   
 
For example, if you want to print a message only if a variable x is greater than 10:

 x = 15

if x > 10:
    print("x is greater than 10")
```

### ii. `if-else` Statement

The `if-else` statement extends the `if` statement by providing an alternative block of code to execute if the condition is false.

```python
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false 
```

For instance, printing different messages based on whether a number is even or odd:

```python
number = 7

if number % 2 == 0:
    # if number divided by 2 leaves a remainder equals to zero(0), it will output "The number is even" if not, "The number is Odd"
    print("The number is even")
else:
    print("The number is odd")
```

### iii. `if-elif-else` Statement

The `if-elif-else` statement is used when you have multiple conditions to check. It allows you to specify multiple blocks of code to execute based on different conditions.

```python
if condition1:
    # Code to execute if condition1 is true
elif condition2:
    # Code to execute if condition2 is true
else:
    # Code to execute if none of the conditions are true
```

An example could be grading students based on their scores:

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")
```

### iv. Nested Conditions

You can nest conditions within each other to handle more complex scenarios. This is similar to having `if` questions inside other `if` questions.

```python
if condition1:
    if condition2:
        # Code to execute if both condition1 and condition2 are true
    else:
        # Code to execute if condition1 is true and condition2 is false
else:
    # Code to execute if condition1 is false 
```

Nested conditions allow you to create intricate decision trees to handle various situations in your program.

## - Loops

- Loops in Python are used for repetitive execution of a block of code. There are two main types of loops: `for` loops and `while` loops. They play a crucial role in automating repetitive tasks and iterating over data structures. Let's explore both types with real-life examples.

## i. `for` Loop

The `for` loop is used to iterate over a sequence (list, tuple, string, etc.) and execute a block of code for each item in the sequence.

### Example: Printing Items in a Shopping List

```python
shopping_list = ["apple", "banana", "chocolate", "water"]

for item in shopping_list:
    print(f"Buy {item}")
```

## ii. `while` Loop

- The while loop continues to execute a block of code as long as a specified condition is true.
- For example: Simple Password Authentication. 

```python
correct_password = "password"
attempts = 3

while attempts > 0:
    user_input = input("Enter your password: ")
    
    if user_input == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")

    if attempts == 0:
        print("Account locked. Too many incorrect attempts.")

```

- In this example, the while loop simulates a simple user login system. The user has three attempts to enter the correct password. The loop provides feedback on incorrect attempts and locks the account after too many failures.

- These examples demonstrate the practical use of loops in Python, making your code more efficient and allowing for the automation of repetitive tasks.

## - Numbers

In Python, **numbers** can be categorized into different types, including integers and floating-point numbers. Understanding how to work with these types is fundamental for various applications.

## i. Integers

Integers are whole numbers without a fractional component. They can be positive or negative.

### Examples:

```python
# Whole number (integer) examples
positive_integer = 5
negative_integer = -3
zero = 0

print("Positive Integer:", positive_integer)
print("Negative Integer:", negative_integer)
print("Zero:", zero)
```

## ii. Floating-Point Numbers

Floating-point numbers have a decimal point, or they can be expressed using scientific notation.

- Examples:

```python
simple_float = 3.14
scientific_notation = 2.5e2  # 2.5 times 10 to the power of 2

print("Simple Float:", simple_float)
print("Scientific Notation:", scientific_notation)
```

## iii. Complex Numbers

Python supports complex numbers, which have a real and an imaginary part.

- Example:

```python
# Complex number example
complex_number = 3 + 2j

print("Complex Number:", complex_number)
print("Real Part:", complex_number.real)
print("Imaginary Part:", complex_number.imag)
```

## - Strings

### 1. String Basics

- Strings are sequences of characters in Python, and they are used to represent text. Understanding how to manipulate and work with strings is essential for a wide range of applications.

- In Python, you can define strings using single (' '), double (" "), or triple (''' ''' or """ """) quotes.

- Examples:

```python
# String definition examples
single_quotes = 'Single quotes'
double_quotes = "Double quotes"
triple_single_quotes = '''Triple single quotes'''
triple_double_quotes = """Triple double quotes"""

print(single_quotes)
print(double_quotes)
print(triple_single_quotes)
print(triple_double_quotes)
```

### ii. String Concatenation

- Concatenation is the process of combining strings.
- Example:

```python
# String concatenation example
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print("Full Name:", full_name)
```

### iii. String Indexing and Slicing

- Strings are sequences, and you can access individual characters using indexing and extract substrings using slicing.

- Example:
```python
# String indexing and slicing example
message = "Hello, World!"

# Indexing
first_char = message[0]
print("First Character:", first_char)

# Slicing
# message[7:12] means it will start from index 7 but not including index 12. 

substring = message[7:12]
print("Substring:", substring)
```

### String Methods

- Python provides a variety of built-in string methods for string manipulation.
- Example:

```python
sentence = "God is the almighty in His Ways"

# Uppercase
uppercase_sentence = sentence.upper()
print("Uppercase: ", uppercase_sentence)

# Replace
modified_sentence = sentence.replace("almighty", "Powerful")
print("Modified Sentence: ", modified_sentence)
```

## - Lists

- Lists are one of the most versatile and widely used data structures in Python. They are ordered collections that can hold a variety of data types. Understanding how to work with lists is fundamental for many applications. 
- Lists are mutable, meaning you can change their contents by adding or removing elements unlike "Tuples". 

### i. List Basics

- In Python, lists are defined using square brackets `[]`.
- Example:

```python
# List definition example
fruits = ["apple", "banana", "cherry", "date"]

print("List of Fruits:", fruits)
```

### i. Accessing Elements in a List

- Elements in a list can be accessed using indexing:
- For Example:

```python
# Accessing elements in a list example
first_fruit = fruits[0]
second_fruit = fruits[1]

print("First Fruit:", first_fruit)
print("Second Fruit:", second_fruit)
```

## - Tuples

- Tuples are ordered, immutable sequences in Python. Once created, the elements of a tuple cannot be changed or modified. They are commonly used to store related pieces of information.
- Tuples and lists looks similar in presenatation. The difference is with tuples, the values is presented inside parenthesis `()` while lists are presented inside sqare brackets`[]`
- Example

```python
# Creating a tuple with different data types
mixed_tuple = (1, "apple", 3.14, True)

# Creating a tuple with similar data types
fruits_tuple = ("apple", "banana", "orange")
```

## - Dictionary

- Dictionaries in Python are powerful data structures that allow you to store and retrieve data using **key-value pairs**.
- They are unordered, mutable, and versatile, making them suitable for a wide range of applications.

## Creating Dictionaries 🌐

```python
# Creating a dictionary with key-value pairs
student_info = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}
```

- To access and modify dictionaries, here's an example below.

- ### Accessing values using keys

student_name = student_info["name"]
student_age = student_info["age"]

- ### Using the get() method

student_grade = student_info.get("grade", "N/A")

- ### Modifying values

student_info["age"] = 26

- ### Adding new key-value pairs

student_info["gender"] = "Female"

- ### Removing key-value pairs

del student_info["grade"]

## - Dictionary Functions

### Getting keys and values

keys = student_info.keys()
values = student_info.values()

### Checking membership

is_grade_present = "grade" in student_info

## - DateTime()

- `datetime` is a module in Python that provides classes for working with dates and times. It allows you to perform various operations, such as formatting dates, calculating differences, and working with time zones.

- Importing `datetime` 📚

```python
# Importing the datetime module
from datetime import datetime, timedelta
```

- Getting the current date and time

```python
current_datetime = datetime.now()
```

- Formatting a datetime object as a string

```python
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
```

- Calculating the difference between two dates

```python
other_datetime = current_datetime + timedelta(days=5)
time_difference = other_datetime - current_datetime
```

## - Functions

- Functions in Python allow you to encapsulate a block of code, making it reusable and modular. They enhance code readability and maintainability by breaking down complex tasks into smaller, manageable pieces.

- How does on define functions? 

```python
# Defining a simple function
def greet(name):
    """A function that greets the user."""
    print(f"Hello, {name}!")
```

- To call the function, we can say

```python
greet ("Alice")
```

### Functions with multiple parameters.

def add_numbers(x,  y):
   """A function that adds two numbers"""
   return x + y

## - Modules

- Modules in Python are files containing Python code that define functions, variables, and classes.
- They allow you to organize code into separate files, making it more modular and maintainable.
- Python comes with a rich standard library of modules, and you can also create your own.

## Importing Modules 🌐

```python
# Importing the entire module
import math

# Importing specific functions or classes from a module
from math import sqrt, pi
```

### Using Standard Library Modules 📚

- Example:

```python
# Using the math module
radius = 5
area = math.pi * math.pow(radius, 2)
```

### Creating Your Own Modules 🛠

```python
# creating a custom module(my_module.py)
#Contents of my my_module.py:
# def greet(name):
#     print(f"Hello, {name}!")

# Using the custom module,
from my_module import greet
greet ("Alice")
```

### Module Aliasing 🚀

 ```python
 # Aliasing a module for a shorter name
 import math as m

 # Using the imported aliased module
 result = m.sqrt(25)
```

## - Exceptions

- Exceptions in Python are events that occur during the execution of a program and disrupt its normal flow. They are raised when an error or exceptional condition occurs, and they can be caught and handled to prevent program termination.

- Handling Exceptions 🛡

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handling the specific exception
    print(f"Error: {e}")
except Exception as e:
    # Handling other exceptions
    print(f"Unexpected error: {e}")
finally:
    # Code that will be executed no matter what
    print("Cleanup code")
```

- ### Raising Exceptions ⚠️

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

- ### Custom Exceptions 🧑‍💻

```python
class CustomError(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

# Raise a custom exception
try:
    raise CustomError("This is a custom exception")
except CustomError as ce:
    print(f"Caught custom exception: {ce}")

```

### Exception Handling Best Practices 🌐

- **Specificity**: Handle specific exceptions rather than using a broad except block.
- **Cleanup**: Utilize finally for cleanup code that should run regardless of whether an exception occurred.
- **Logging**: Consider logging exceptions to aid debugging.
- **Custom Exceptions**: Create custom exceptions for specific error conditions in your application.
- **To be Continued**