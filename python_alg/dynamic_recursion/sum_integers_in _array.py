# Given an array, [5,4,3,6,10] and int 14
# Find the number of subsets in the array that add up to the int

# There are no negative numbers in the array
# We need to start at one end of the array, and check if any other value or values in the rest of the array add up to target
def find_subs(array, target):
    if len(array) == 1:
        if array[0] == target:
            return 1
        else:
            return 0
    store = {}
    find_combinations(array, target, store)

def find_combinations(array, target, index, store):
    if target == 0:
        return 1 # one empty set sums to 0
    if target < 0:
        return 0
    key = str(target) + "-" + str(index)
    if key in store:
        return store[key]
    else:
        new_target = target - target[index]
        result = find_combinations(array[:index], new_target, index-1, store)
    
