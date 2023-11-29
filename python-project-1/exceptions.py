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
    
    
######------ Exercise to handle exceptions for age ----#######

# first we define a function

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

## In this example, the safe_divide function attempts to divide two numbers and gracefully handles the ZeroDivisionError by returning an error message.

def safe_divide(x, y):
    try:
        result =x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    
# example usage
result = safe_divide(10, 0)
print(result)
