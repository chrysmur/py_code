'''
A monotonic a array is a n array that is either exclusively non-increasing or exclusively non-decreasing
Having same number appear twice in a row does not invalidate these conditions, i.e the array can still be monotonic because
the two numbers are neither showing increase nor decrease

'''

def isMonotonic(array):
    # Write your code here.
	if len(array) < 2:
		return True
	non_dec = None
	non_inc = None
	for i in range(len(array)-1):
		if array[i] < array[i+1]:
			non_dec = True # if we encounter rise, we set true
		elif array[i] > array[i+1]:
			non_inc = True # if we encounter drop, we set true
		
	if non_dec and non_inc: # we should not have both up and down
			return False
	return True

print(isMonotonic([5,5,4,3,2]))