#!/usr/bin/python3
def rotate(A, K):
    N = len(A)
    i = 0
    A_dict = {i: A[i] for i in range(N)}
    for i in range(N):
        pos = i + K
        new_pos = pos % N
        A[new_pos] = A_dict[i]
    
    return A
print(rotate([3,4,5,6,7,8,8], 9))