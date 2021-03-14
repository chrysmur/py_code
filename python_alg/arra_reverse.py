#!/usr/bin/python3
# Reverse an array in memory

def reverse(array):
    if type(array) != list:
        return "Pass an array"
    N = len(array)
    for i in range(N//2):
        r_i = N-i-1
        array[i], array[r_i] = array[r_i], array[i]
    return array

print(reverse([1,2,3]))