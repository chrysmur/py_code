'''
use sieve of eratostenes to calculate all prime numbers from 2 to inf
@computerphile youtube
'''

def get_prime(n):
    yield n
    yield from get_prime(n+1)

def sieve(s):
    next_prime = next(s)
    yield next_prime
    yield from sieve( i for i in s if i%next_prime )

prime = get_prime(2)
p = sieve(prime)
print(next(p)) #2
print(next(p)) #3
print(next(p)) #5
print(next(p)) #7
print(next(p)) #11