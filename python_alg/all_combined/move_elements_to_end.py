'''
Given an array array of integers and an integer,
Move all instances of the integer to the end of the array
'''

def moveElementToEnd(array, toMove):
    # for we keep track of last item to to terminate the loop
    # by incrementing i, if we get the integer, we split the array and append the integer to the right side
    O(N^2)
    i = 0
	N = len(array)
	j = N -1
	while i <= j:
		if array[i] == toMove:
			left = array[:i]
			right = array[i+1:]
			right.append(toMove)
			array = left + right
			j -= 1
		else:
			i += 1
	return array

#O(N), O(N) space
def moveElementToEnd2(array, toMove):
    # Write your code here.
	new_array = []
	instances = 0
	for value in array:
		if value != toMove:
			new_array.append(value)
		else:
			instances += 1
	return new_array + [toMove]*instances

#The above methods works if we need to maintain the order of the other elements in the array
# if not, we can swap
def moveElementToEnd3(array, toMove):
    # Write your code here.
    #O(N), Space O(1)
	i = 0
	j = len(array) - 1
	while i < j:
		if array[i] == toMove and array[j] != toMove:
			array[i], array[j] = array[j], array[i]
			i += 1
			j -= 1
		elif array[i] != toMove:
			i += 1
		elif array[j] == toMove: #else
			j -= 1
			
	return array