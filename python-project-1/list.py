# list of fruits
fruits = ["apple", "banana", "pawpaw", "watermelon"]
print("List Of Fruits:", fruits)

first_fruit = fruits[0]
second_fruit = fruits[3]

print("What's the first fruit on the list? ", first_fruit)
print("What's your favorite fruit on the list? ", second_fruit)

# lets update the list 3th index which is 'watermelon' to 'pinapple',
# How can that be done?
fruits[3] = "pinapple"
print(fruits)

# How can we delete an item from the list? lets delete banana in our case. cus i don't really like bananas. 
print("---")
print("Banana will be taken out of the list")
del fruits[1]
print(fruits)