'''
Given an integer, and given that it is an encorded message from the map of 1: a, 2: b ...26:z
Find how many ways you can decode the message
0 is not part of the encoding

>> 
'''

def decodeways(s,k, memo = {}):
    if k == 0:
        return 1
    if s == '':
        return 0
    if s in memo:
        return memo[s]
    N = len(s)
    decode = decodeways(s[1:], k-1, memo) # decoce one by one
    if len(s) >= 2 and int(s[:2]) <= 26:
        decode += decodeways(s[2:], k-2, memo) # decode two by two because 11-26 is double digits
    memo[s] = decode
    return decode

def decoder(integer):
    s = str(integer)
    ways = decodeways(s, k= len(s))
    return ways


print(decoder(123))