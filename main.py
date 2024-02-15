from art import logo
print(logo)

print("Welcome To The Blind Auctionn\n")

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bidding amount of ${highest_bid}")


while not bidding_finished:
    name = input("Enter the name of bidder: ")
    bid_amount = int(input("Enter the bid amount: "))
    bids[name] = bid_amount
    more_bidders = input("Are there more bidders ?: ").lower()
    if more_bidders=="no":
        bidding_finished = True
        highest_bidder(bids)
    else:
        continue
    
    