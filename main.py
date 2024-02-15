from art import logo
print(logo)

print("Welcome To The Blind Auctionn\n")

bids = {}
bidding_finished = False

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
    
    