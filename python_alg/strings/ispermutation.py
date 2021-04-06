'''
Given strings 1 and 2, find if they are permutations of each other
'''

def isperm(str1, str2):
    # O(nlog(n))
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    #sorting the strings
    str1 =  ''.join(sorted(str1))
    str2 =  ''.join(sorted(str2))

    n = len(str1)
    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True

print(isperm("cat", "at"))


def isperm2(str1, str2):
    # O(n) time and space
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    d = dict()
    for i in str1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in str2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())

print(isperm2("cat", "act"))