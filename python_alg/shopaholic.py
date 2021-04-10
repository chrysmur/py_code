'''
A shopaholic has to buy a pair of jeans, a pair of shoes, a skirt, and a top with budgeted dollars. 
Given a list of prices for each kind of product, determine how many different combinations can be bought.
If required, all budgeted dollars can be spent.

Input
The input consists of five lines. 
The first four lines represent the possible prices of jeans, shoes, skirts, and tops, respectively.
Each line starts with an integer k (1≤k≤1000), followed by k integers pi, 
each representing the price of one of the available choices (1≤pi≤109).

The fifth line contains a single integer B (1≤B≤109), 
representing the total overall budget.

Example
2 2 3  jeans
1 4 shoes
1 2 skirts
3 1 2 3 tops
10

'''
def max_combinations(prices, budget):
    from itertools import product
    combo = [price for price in list(product(*prices)) if sum(price) <= budget]
    print(len(combo))




if __name__ == "__main__":
    # jeans = list(map(int,(input("Enter jeans prices: ").split())))
    # shoes = list(map(int, input("Enter shoes prices: ").split()))
    # skirts = list(map(int, input("Enter skirts prices: ").split()))
    # tops = list(map(int, input("Enter tops prices: ").split()))
    # budget = int(input("Enter budget: "))

    #prices = [jeans, shoes, skirts, tops ]
    prices =[[ 2, 3], [1, 4], [1, 2], [3, 1, 2, ]]
    budget = 10
    print(max_combinations(prices, budget))