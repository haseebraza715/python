line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print("chose between a1 , a2 , a3 , b1 , b2 , b3, c1, c2, c3 ")
position = input() 
# Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if(position == "a1"):
    map[0][0] = "X"
elif(position == "a2"):
    map[1][0] = "X"
elif(position == "a3"):
    map[2][0] = "X"
elif(position == "b1"):
    map[0][1] = "X"
elif(position == "b2"):
    map[1][1] = "X"
elif(position == "b3"):
    map[2][1] = "X"
elif(position == "c1"):
    map[0][2] = "X"
elif(position == "c2" ):
    map[1][2] = "X"
elif(position == "c3"):
    map[2][2] = "X"    
else:
    print("give the appropiate value")


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")