import random
#in this one we ll talk about list and their respective functions and methods

grades = [1,3,4,4,4,4,4,4,4,4]
print(grades)

#and list can be of any type string int floating number stuff like that 
#so first we make trhe string and then convert it into list and then
arr_string = "haseeb ,hasss ,jsdhjshdjshd"
names =arr_string.split(',')
#we use the random method using the indexes of it to choose the random number
length_names = len(names)
print(length_names)
rand = random.randint(0, length_names-1)
print(names[rand] + "is going to pay the bills")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0][3])




