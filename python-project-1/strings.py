# lets define some variables
# Remember to always wrap strings in quotes

first_name = "Abri" 
last_name = "Fuh"

full_name = first_name +" " + last_name # " ": This is a string literal containing a single space. It's used as a separator between the first and last names.
# OR
full_name = f"{first_name} {last_name}" #You could also use formatted strings (f-strings) for a more concise and readable syntax in Python 3.6 and later
print(full_name)

# User input and string manipulation
user_name = input("Enter your Name: ")
greeting = "Hello, " + user_name + "!"
print(greeting)

sentence = "God is the almighty in His Ways"

# Uppercase
uppercase_sentence = sentence.upper()
print("Uppercase: ", uppercase_sentence)

# Replace
modified_sentence = sentence.replace("almighty", "Powerful")
print("Modified Sentence: ", modified_sentence)