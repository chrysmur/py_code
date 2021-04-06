'''Determine if it is possible to move from start to he end if each value in the array represent  the max number of steps you can move from the point
Alg A = [3,2,0,0,2,0,1]
A[0] + index == 3 + 0 = the furthest we can get, 3
A[1] + index == 2 + 1 = equal to the furthest from round 1, 3
A[2] + index == 0 + 2 = less than the furthest we have so far, 2
A[3] + index == 0 + 3 =  equal to the furthest from above, 3
A[4] + index... index is greater than furthest, return False


A= [3,3,0,1,2,0]
A[0] + index == 3 + 0 = 3
A[1] + index == 3 + 1 =  4
A[2] + index == 0 + 2  = 2*
A[3] + index == 1 + 3 = 4 same
A[4] + index == 2 + 6 = 6
A[5]: furthest is greater than last index, return True
'''
 
def can_advance(array):
    furthest = 0
    n = len(array)
    for index, value in enumerate(array):
        if index > furthest:
            return False
        max_adv = value + index
        furthest =  max(max_adv, furthest)
        if furthest >= n:
            return True
        
# By LucidProgramming Youtube
def can_advance2(A): 
    furthest_reached = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_index

print(can_advance([3,3,0,1,2,0]))
print(can_advance([3,2,0,0,2,0,1]))
print(can_advance([3,3,0,1,2,0]))