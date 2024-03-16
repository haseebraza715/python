#linear search algorithm 
def isEven(a):
    if (a % 2 == 0):
        return True
    else:
        return False

list = [1,5,3,4,5,6]

l = False
i = 1

while(i <= len(list) and l == True):
    l = isEven(list[i])
    ind = i
    i = i + 1 

print(l)
 
#print(ind)
    

    