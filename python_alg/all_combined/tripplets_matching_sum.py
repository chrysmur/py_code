'''
Given an array of numbers including negatives, and a targetsum, return all possible triplets that sum up to the targetsum
'''
from itertools import combinations

#solution 1 using itertools combinations
def threeNumberSum(array, targetSum):
    # Write your code here.'
	all_comb = list(combinations(array, 3))
	targets = []
	for combo in all_comb:
		if sum(combo) == targetSum:
=			targets.append(sorted(combo))
	return sorted(targets)

# better solution: Algoexpert O(N^2)
def threeNumberSum2(array, targetSum):
    array.sort()
    triplets = []
    N = len(array)
    for index in range(N - 2):
        rem = targetSum - array[index]
        i = index + 1
        j = N - 1
        while i < j:
            two_sum = array[i] + array[j] 
            if two_sum == rem:
                trip = [array[index], array[i], array[j]]
                triplets.append(trip)
                i += 1
                j -= 1
            elif two_sum < rem:
                i += 1
            elif two_sum > rem:
                j -= 1
    return triplets