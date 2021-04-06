## Erite a function that receives a target sum and a list of numbers, 
# return true or false if it is possible to generate the targetsum from the array
# elements can be used as many times as possible,
# you may assume that all input numners are non negative

'''
cansum(5, [4,3,2,5]) => true  [5] or [2,3]
Can you do it? yes or no--> it is a DECISION Problem
'''
def cansum(target, array, store={}):
    if target == 0: 
        return True
    if target < 0: 
        return False
    for num in array:
        remainder = target - num
        # we can reuse the numbers, we call with same array
        if remainder in store:
            return store[remainder]
        result =  cansum(remainder, array, store)
        store[remainder] = result
        if result == True:
            return True
            
    return False

        # If we did not have to repeat the numbers, we'd call with array after poping num

print(cansum(7,[2,3]))
print(cansum(7,[5,3, 4,7]))
print(cansum(7,[2,4]))
print(cansum(300,[7,14]))