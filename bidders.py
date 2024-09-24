from replit import clear

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print('Congratulations!')
    print(f'The winner is {winner} with a bid of ${highest_bid}')

bids = {}

bidding_finished = False
while not bidding_finished:
    name = input("What's your name? ")
    price = int(input('What\'s your bid price? $'))
    bids[name] = price
    
    should_continue = input('Are there any bidders? Type \'yes\' or \'no\' : ')
    if should_continue == 'no' or should_continue == 'n':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes' or should_continue == 'y' or should_continue == 'ye':
        clear()


    
