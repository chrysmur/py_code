'''
There are potholes on the road whose locations are given by X and Y coord where the X is across the road and y is along the road
The roller filling the holes moves from the end of the road along the Y axis to the end, and back the same way covering the width given by W
Find the minimum number of trips the roller will move have to move to fill all the potholes
'''
def potholes(X,Y, W):
    sorted_x = list(set(X)) #O(n)
    sorted_x.sort() #O(nlogn)

    counts = 0
    furthest = 0
    N = len(sorted_x)
    i = 0
    while i < N: #O(n)
        current = sorted_x[i]
        if current > furthest:
            counts+= 1
            furthest = current + W
        i += 1
    return counts



print(potholes([4,8,2,2,1,4],[],3))


