'''
OPTIMIZATION
Suppose you are a programmer for a vending machine manufacturer.
 Your company wants to streamline effort by giving out the fewest possible coins in change for each transaction. 
 Suppose a customer puts in a dollar bill and purchases an item for 37 cents. 
 What is the smallest number of coins you can use to make change?
'''

def min_change(coins, change, memo = {}):
    # base case
    if change in memo: return memo[change]
    if change in coins: return 1
    
    mincoins = change

    for coin in [c for c in coins if c<=change]:
        remainder = change - coin
        num_coins = 1 + min_change(coins, remainder, memo)
        if num_coins < mincoins:
            mincoins = num_coins
    memo[change] = mincoins
    return mincoins




print(min_change([1,5, 10, 25], 63))
