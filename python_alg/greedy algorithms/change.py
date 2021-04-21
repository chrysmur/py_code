'''
Given the us currency values, find the minimum number of coins necessary to give change
'''

def change_making(cents):
    COINS = [100, 50, 25, 10, 5, 1]

    num_coins = 0

    for coin in COINS:
        num_coins += cents // coin
        cents %= coin

    return num_coins

c =  863
print(change_making(c))

