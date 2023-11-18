# This code verifies the age of persons wanting to enter a club. 
# As we know, for most clubs in canada, it requires that you are a certain age for you to be eligible to enter. 


print ("Welcome to Cabana Night Club!!")
# Guest is suppose to respond by inputing thier age. 
# In python, we can do this for guest to enter thier age. 
age = int(input("How old are you? "))
if age >= 21:
 print ("Welcome to our Club...")
elif age >= 18:
  print ("Cannot Enter until you are 21 ")
else:
  print("Sorry You are still a Kid ...")


