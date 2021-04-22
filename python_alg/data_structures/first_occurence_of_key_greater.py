'''
Design an efficient algorithm that takes a sorted array and a key, and finds the index of
the first occurrence of an element greater than that key
'''
# we need to find the last occurence of k

def search_first_of_greater_k(A, k):
    left, right, result =  0, len(A) - 1, -1

    while left <= right:
        mid =  (left + right) // 2
        if k < A[mid]:
            right =  mid - 1
        elif k == A[mid]:
            left = mid + 1
            result  =  mid+1
        else: # if k > mid
            left = mid + 1

    return result



A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 403]
print(search_first_of_greater_k(A, 285))
