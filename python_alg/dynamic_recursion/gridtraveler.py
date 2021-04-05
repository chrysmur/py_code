
## How many ways can you travel from top left to bottom right of a nxm grid and you can only move down and right
'''
eg, 2,3 move right (2,2),move right (1,2),
        move down  (1,3)
'''
def gridtraveler(m,n, store={}):
    if m == 1 and n == 1:
        return 1 # base solution, when you land in the last box
    if m == 0 or n == 0:
        return 0 # you are stack, its not a solution
    key = str(n) + '-' + str(m)
    if key in store:
        return store[key]
    store[key] =  gridtraveler(m-1, n, store) + gridtraveler(m, n-1, store)
    return store[key]
    
'''
the depth of the this tree is n+3
time O(2^n+m) without memoization
space O(n+m)
[1,2] and [2, 1] has same result so we only need to store one in memory

with m, n = 3,2
m forms {0,1,2,3}
n forms  {0,1,2}
Form complexity, since we have memomized the lower level nodes, we can only travel through m * n combinations 
O(n*m) is the time complexity
O(n+m) is the space complexity
'''
print(gridtraveler(1,2))
print(gridtraveler(5,5))
print(gridtraveler(2,2)) 
print(gridtraveler(3,3))
print(gridtraveler(18,18))

