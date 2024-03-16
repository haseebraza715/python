print(
    ''' 
 .-.  .-.  --..::==
(   )(   )  //"
 '-'  '-'  /

'''
)


#this is Treasure Island game
print("Welcome to Treasure Island.Your mission is to find the treasure")
#wheter it is left or right 
print("Choose Between left and right")
option = input("left or right: ")
if(option == "left"):
    print("You want to swim or wait Choose Shawty :)")
    option2 = input("swim or wait: ")
    if(option2 == "wait"):
        print("Choose the Color of Door: Red , Blue , Yellow")
        option3 = input("which door: ")
        if(option3 == "Red"):
            print("Burned by Fire. Game Over")
        elif (option3 == "Blue"):
            print("Eaten by beasts. Game Over")
        elif (option3 == "Yellow"):
            print("You Win..... woah ")
        else:
            print("Game Over")

    else: 
        print("Attacked by trout. Game Over.")                        
else:
    print("Fail into Hole Game Over")
