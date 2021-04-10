'''
Given two sorted arrays,  find the intersection
'''

def intersection(A, B):
    #return set(A).intersection(set(B))
    i = j = 0
    inters = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if A[i] != A[i-1]:
                inters.append(A[i])
            j += 1
            i += 1
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return inters


A = [2,3,3,5,7,11]
B = [3,3,7,15,31]
print(intersection(A,B))
