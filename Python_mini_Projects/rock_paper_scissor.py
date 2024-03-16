import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the ROCK-PAPER-SCISSORS GAME")
print("what do you chooose 0 for rock 1 for paper 2 for scissors")
possible_values = [rock,paper,scissors]
per_choice = int(input())
print("User Chooses")
if per_choice > 3 and per_choice < 0:
    print("You choose the inavlid number")
else:
    print(possible_values[per_choice])


comp_random = random.randint(0, 2)
print("Computer Choose: ")
print(possible_values[comp_random]) 

if per_choice > comp_random:
    print("You Win")
elif per_choice == comp_random:
    print("You draw")
elif per_choice == 0 and comp_random == 2:
    print("You Win")
elif comp_random == 0 and per_choice == 2:
    print("You lose")
elif comp_random > per_choice:
    print("You lose")     



#rock(0) win scicssors(2)
# 1 2 
#scicssor(2) win paper(1)
#paper(1) win rock(0)
#so what you choose 0 for rock 1 for paper 2 scissors
#lets makes two list one for the user and one for the computer and then we ll use random for the 
#computer to choose randomly 
#0 > 1 = win 
#lets use random for the computer    






