'''
Find the product of two numbers  using recursion

'''
def product(x,y, store={}):
    if x in store: return store[x]
    if y == 1:
        return x
    if x == 0 or y == 0:
        return 0    
    
    min_prod = product(x, y-1,store)
    store[x] = x + min_prod
    return  store[x]


# iterative soln:
def product_it(x, y):
    if y == 1:
        return x
    if x == 0 or y == 0:
        return 0 
        
    prod = 0
    for i in range(y):
        prod += x
    return prod

print(product(5000,4352))
