'''
A function that takes in any two none empty arrays of integers, find the numbers from each array whose absolute difference is closest to zero
'''
#O(NLogN)
def smallestDifference(arrayOne, arrayTwo):
	array1 = arrayOne
	array2 = arrayTwo
    array1.sort()
    array2.sort()

    i = 0 
    j =  0
    min_value = float("inf")
    min_combo = []
    while i < len(array1) and j < len(array2) :
        ar1 = array1[i]
        ar2 = array2[j]
        if ar1 > ar2:
			diff = ar1 -  ar2
			if diff < min_value:
				min_value = diff
				min_combo = [ar1, ar2]
            j += 1
        elif ar2 > ar1:
            diff = ar2 -  ar1
			if diff < min_value:
				min_value = diff
				min_combo = [ar1, ar2]
			i += 1
		else:
			min_value = 0
			min_combo = [ar1, ar2]
			i += 1
			j += 1

    return min_combo


