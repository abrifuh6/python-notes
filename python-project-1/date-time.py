# Consider a task management system where you want to track the due date of tasks

# Importing the datetime module
from datetime import datetime

task = {
    "name": "Complete Python Notes",
    "due_date": datetime(2023, 12, 1, 18, 0, 0) # Due date is December 1, 2023, at 6:00 PM
}

# Checking if the task is overdue
is_overdue = task["due_date"] < datetime.now()

# Printing the result
print(is_overdue)