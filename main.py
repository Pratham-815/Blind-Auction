from art import logo
print(logo)

print("Welcome To The Blind Auctionn\n")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("Enter the name of bidder: ")
    bid_amount = int(input("Enter the bid amount: "))
    bids[name] = bid_amount
    