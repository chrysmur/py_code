'''
Find the peak of the bitonic sequence
x1, x2, ... <= xk >= ...xn-1
1,2,3,4,5,4,3,2,1 peak  5


'''

def peak_bitonic(A):
    low = 0
    high = len(A) - 1

    #Needs at least 3 elements to be a seq
    if len(A) < 3:
        return None

    while low <= high:
        # mid point of the array
        mid = (low + high) // 2
        
        #Get the value on the left and right side of mid
        mid_left = A[mid-1] if mid-1 > 0 else float("-inf")
        mid_right = A[mid+1] if mid+1 < len(A) else float("inf")

        # if the adjacent value on the left of mid is greater than mid, the the peak is to the left, we move high to  mid
        # if the adjancent value to the right is  greater than  mid, then the peak is to the right, so we move low to mid
        # This way we half the array for every cycle (O(logn))
        if mid_right > A[mid]:
            low = mid+1
        elif mid_left > A[mid]:
            high = mid -1
        
        else:
            return A[mid]
            

print(peak_bitonic([1,6,5,4,3,2,1]))
print(peak_bitonic([3,4,5,9,2,1]))
