import os

dict_bids = {}
highest_bid = 0
highest_bidder = ""

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    if name in dict_bids:
        print("Name already exist")
    else:
        dict_bids[name] = bid

    yes_no = input("Are there any other bids? (Yes/No)")
    if yes_no.lower()=='no':
        break
    else: 
        os.system('cls')

print()
for key,val in dict_bids.items():
    if val > highest_bid:
        highest_bid = val
        highest_bidder = key

print(f"Highest bidder is {highest_bidder} with a bid of ${highest_bid}")

