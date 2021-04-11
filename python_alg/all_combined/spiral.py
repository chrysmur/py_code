def spiralTraverse(array):
    # Write your code here.
	if len(array) == 0:
		return []
	if len(array) == 1:
		return array[0]
	if len(array) == 2:
		return array[0] + array[1][::-1]
	N = len(array)
	mid_last = []
	mid_first = []
	all_array = []
	remainder_array = []
	i = 0
	j = N - 1
	first = array[i]
	last = array[j][::-1]
	for arr in array[1:-1]:
		if len(arr) == 1:
			mid_last.append(arr[0])
		else:
			mid_last.append(arr[-1])
			mid_first = [arr[0]] + mid_first
			if len(arr) > 2:
				remainder_array.append(arr[1:-1])
	
	all_array = first + mid_last + last + mid_first
	return all_array + spiralTraverse(remainder_array)
