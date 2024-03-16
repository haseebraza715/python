import art

print(art.logo)

new_bidd = True
list_of_bidder = []

print("Welcome to the secret auction program.")
while(new_bidd):
    name = input("What is your name?: ")
    bid = int(input("What is your bid:" ))
    new_bid = input ("Are there any other bidders? Type 'yes' or 'no'.")


    new_dic = {}

    new_dic = {
        "name":name,
        "bid" :bid
    }
    
    list_of_bidder.append(new_dic)

   
    if(new_bid.lower() == "no"):
        new_bidd = False

print(list_of_bidder)


def maximum(bidder_list):
    max_bid = 0
    max_bidder_name = ""
    for list in bidder_list:
        current_bid = list["bid"]
        if(current_bid > max_bid):
            max_bid = current_bid
            max_bidder_name = list["name"]
    return max_bid, max_bidder_name


max_bid,max_bidder_name = maximum(list_of_bidder)


print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")



