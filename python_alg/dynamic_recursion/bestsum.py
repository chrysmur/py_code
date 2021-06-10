'''
Given a target and an array, return the shortest combination that sum up to target
The question of Who can do it best, OPTIMIZATION problem
'''

def bestsum(target, numbers):
    if target == 0: return []
    if target < 0: return None

    shortest = None

    for num in numbers:
        remainder = target- num
        result = bestsum(remainder, numbers)
        if result is not None:
            combination = [*result, num]
            if not shortest or (len(combination) < len(shortest)):
                shortest = combination
        
    return shortest



def bestsummemo(target, numbers, store={}):
    if target in store: return store[target]
    if target == 0 : return []
    if target < 0: return None

    shortest  = None
    for num in numbers:
        if num < 0:
            return "Invalid Input"
        remainder = target - num
        result = bestsummemo(remainder, numbers, store)
        if result is not None:
            combination = [*result, num]
            store[target] = combination
            if not shortest or len(combination) < len(shortest):
                shortest = combination
    return shortest


print(bestsummemo(15, [7,10,16,-1]))