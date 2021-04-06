'''
Given a sorted array of integers, return the two numbers such that they add up to a target

'''

def two_sum1(A, target):
    # using hash table space O(N), time O(N)
    d = {}
    for value in A:
        diff =  target - value
        if diff in d:
            print(diff, value)
            return True
        else:
            d[value] =  value
    print(d)
    return False

def two_sum2(A, target):
    #Constact space, O(n) time
    # Since it is sorted
    i = 0
    j = len(A)-1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        if A[i] + A[j] > target:
            j -= 1
        else:
            i += 1

print(two_sum2([3,4,5,6], 11))