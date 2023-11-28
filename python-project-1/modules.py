# Consider a script that needs to interact with the file system, perform mathematical calculations, and generate random numbers. Instead of writing all this functionality from scratch, you can leverage existing modules:

import os 
import math 
import random 

# get the current working directory
current_directory = os.getcwd
print(current_directory)
# calculate the square root of a number
result = math.sqrt(64) 
print(result)
# Generate a random number between 1 and 10

random_number = random.randint(1, 10)
print(random_number)