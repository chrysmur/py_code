# return the combination from the array that adds up to the target sum
# The numbers can be repeated
'''
Question of who can, which is a COMBINATORIC problem
'''

def whichsum(target, numbers):
    if target ==0 :return []
    if target < 0: return None

    for num in numbers:
        remainder = target - num
        result = whichsum(remainder, numbers)
        if result is not None:
            return [*result, num]

    return None


def whichsummemo(target, numbers, store={}):
    if target in store: return store[target]
    if target == 0 :return []
    if target < 0: return None

    for num in numbers:
        remainder = target - num
        result = whichsummemo(remainder, numbers, store)
        if result is not None:
            store[target] = [*result, num]
            return store[target]
        store[target] = None
    return None
        

print(whichsummemo(7,[2,3]))
#print(whichsummemo(7,[5,3,4,7]))
#print(whichsummemo(7,[2,4]))
#print(whichsummemo(8, [2,3,5]))
#print(whichsummemo(300,[7,14]))

# complexity 
'''
whichsome
m = target
n =  len(numbers)
time = O(n^m * m) exponential
space = O(m)

whichsomememo
time O(n*m^2)
space O(m^2)
'''