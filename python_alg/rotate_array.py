#!/usr/bin/python3

'''
Rotate the Array A K times to the right
rotote([2,3,4], 2) = [3,4,2]
'''
def rotate(A, K):
    N = len(A)
    i = 0
    A_dict = {i: A[i] for i in range(N)}
    for i in range(N):
        pos = i + K
        new_pos = pos % N
        A[new_pos] = A_dict[i]
    
    return A
print(rotate([2,3,4], 2))