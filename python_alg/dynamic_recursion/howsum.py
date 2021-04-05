# Given an array, [5,4,3,6,10] and int 14
# Find the number of subsets in the array that add up to the int

# There are no negative numbers in the array
# We need to start at one end of the array, and check if any other value or values in the rest of the array add up to target


# Numbers can be repeated.
def howsum(target, numbers, store = {}):
    if target in store: return store[target]
    if target == 0: return [[]]
    if target < 0: return None

    combinations = []
    for num in numbers:
        remainder = target - num
        result = howsum(remainder, numbers)
        if result is not None:
            comb = [[*way, num] for way in result]
            store[target] = comb
            combinations.extend(comb)
        
    return combinations

print(howsum(14, [5,4,3,6,10]))