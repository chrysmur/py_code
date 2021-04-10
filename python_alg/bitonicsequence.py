'''
Find the peak of the bitonic sequence
x1, x2, ... <= xk >= ...xn-1
1,2,3,4,5,4,3,2,1 peak  5
We assume that  

'''

def peak_bitonic(A):
    low = 0
    high = len(A) - 1

    #Needs at least 3 elements to be a seq
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = A[mid-1] if mid-1 > 0 else float("-inf")
        mid_right = A[mid+1] if mid+1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid+1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid -1
        
        else:
            return A[mid]
            
def peak_bitonic_re(A):

print(peak_bitonic([1,6,5,4,3,2,1]))

