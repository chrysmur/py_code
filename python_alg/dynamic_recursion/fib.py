## Memoization using hash table
## O(n) time and space
def fib(n, store={}):
    if n <= 2:
        return 1
    if n in store:
        return store[n]
    result =  fib(n-1, store) + fib(n-2, store)
    store[n] = result
    return result

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))