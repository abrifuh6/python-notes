# While loops
# This code is for password login attempts

# Defining password as "password" and number of attempts
correct_password = "password"
attempts = 3

while attempts > 0:
    user_input = input("Enter your password ")
    
    if user_input == correct_password:
        print("Login Successful!")
        break
    
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")