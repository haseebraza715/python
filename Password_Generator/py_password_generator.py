#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_letters = []
for n in range(1,nr_letters+1):
   rand_letters += random.choice(letters)
rand_symbols = []
for n in range(1, nr_symbols + 1):
    rand_symbols += random.choice(symbols)
rand_numbers =[]
for n in range (1, nr_numbers+1):
    rand_numbers += random.choice(numbers)
password = rand_letters + rand_numbers + rand_symbols
print("Here is your Strong Password: ")
print(password)
random.shuffle(password)
print(password)

password_str = ""

for char in password:
    password_str += char

print("Here is your Strong Password in String: " + password_str)

list = ['J','d','u','E','&','!','9','1']



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P