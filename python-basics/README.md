# Python

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
## - Lists
## - Tuples
## - Dictionary
## - DateTime()
## - Functions
## - Modules
## - Exceptions
