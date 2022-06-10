'''
Given an a non negative decimal integer,
add one to the integer. assume that the solution still works for languages with finite precision arithmentic
149 => 150
'''
# without fpa, s = ''.join(map(A, str)), int(s) + 1


def arb_increment(A):
    N =  len(A)-1
    index = N
    while index >= 0:
        value = A[index]
        added = int(value) + 1
        if index == 0:
            A[index] =  str(added)
            break
        if added >= 10:
            A[index] = str(added % 10)
        else:
            A[index] =  str(added)
            break
        index -= 1
    return ''.join(A)


print(arb_increment([9,9,9]))
