import logo
from os import system, name

auction_dictionary = {}
final_bid = False

def clear():
    if name == 'nt':
        _ = system('cls')

def find_highest_bidder(auction_dictionary):
    top_bid = 0
    highest_bidder = ""
    for bidder in auction_dictionary:
        bid = auction_dictionary[bidder]
        if bid > top_bid:
            top_bid = bid
            highest_bidder = bidder
    print(f"Congratulations, {highest_bidder}! You win with a bid of ${top_bid}.")

while not final_bid:
    print(logo.gavel)
    print("Welcome to the Blind Auction Tool.\n")
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_dictionary[bidder] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(auction_dictionary)
    elif should_continue == "yes":
        clear()