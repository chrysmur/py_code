'''
Find the duplicated number
'''

def duplicated(array):
    for i in range(len(array)):
        value =  abs(array[i])
        if array[value] < 0:
            return abs(value)
        array[value] = -array[value]
    return False

print(duplicated([2,3,4,1]))