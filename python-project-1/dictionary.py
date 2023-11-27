# Dictionary is unordered list that stores data using "key-value pairs"
# Here's an example of such
student_info = {
    "first_name" : "John" ,
    "last_name" :" Doe ",
    "age": 20 ,
    "grade" : "A"
}

# student_name = (student_info["first_name"] )
print (student_info["first_name"] )
print(student_info["age"])

student_grade = student_info.get("grade", "N/A")

# Book Database
# Dictionary representing a book and it's various authors
book_info = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

# List of books
book_database = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}
]

print(book_info["title"])

# o retrieve a particular title from the list in the database, you can use the key of the dictionary that represents the book and access the corresponding value
print(book_database[0]["title"])

# OR

# Accessing a particular title from the book database
desired_book_title = book_database[1]["title"]  # Change index (1) as needed

# Printing the result
print(f"The title of the desired book is: {desired_book_title}")

