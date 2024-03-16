def prime_checker(number):
    if number > 100:
        print("Give me number less than 100")
        return
    list_num = list(range(1, number + 1))
    count = 0
    for n in list_num:
        if (number % n == 0):
            count += 1
    if (count == 2):
        print("This is a prime number")
    else:
        print("This is not a prime number")             

n = int(input()) 
prime_checker(number=n)