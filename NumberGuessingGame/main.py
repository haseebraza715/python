import random
from art import logo

'''function for the easy task
Steps for making the easy part of game:
1.First we have to generate the number between 1 and 100
2.Then give the user ten times to chose the number so basically ten times we have to run the same
code
3.apply condition to it if the number is high than that print too high but if the number is
low then we have to print too low
4.After 10 attempt they lose the game
'''

def easy_mode():
    
    list = []
    for num in range(0,101):
        list.append(num)
    rand_num = random.choice(list)
    print("You have 10 attempts to guess the number: ")
    for num in range(10,0,-1):
        user_num = int(input("Make a guess: "))
        if (user_num == rand_num):
            print(f"You got it the number it was {rand_num}")
            break
        elif user_num < rand_num:
            print("Too low")
            print("Guess again")
        elif user_num > rand_num:
            print("Too high")
            print("Guess again")
        print(f"You have {num - 1} attempts to guess the number: ")


def hard_mode():
    list = []
    for num in range(0,101):
        list.append(num)
    rand_num = random.choice(list)
    print("You have 5 attempts to guess the number: ")
    for num in range(5,0,-1):
        user_num = int(input("Make a guess: "))
        if (user_num == rand_num):
            print(f"You got it the number it was {rand_num}")
            break
        elif user_num < rand_num:
            print("Too low")
            print("Guess again")
        elif user_num > rand_num:
            print("Too high")
            print("Guess again")
        print(f"You have {num - 1} attempts to guess the number: ")
    
print(logo)
print("Welcome to the number guessing game")
print("I am thinking of number betweenn 1 and 100")

choice = input("Choose the difficulty easy or hard: ")

if choice == "easy":
    easy_mode()
elif choice == "hard":
    hard_mode()
else:
    print("Please give me the correct input: Thank you")
