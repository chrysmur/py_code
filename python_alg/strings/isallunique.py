'''
Determine if a stirng has all unique characters
'''

def cleanup(string):
    string = string.replace(" ", "")
    return string.lower()

def is_unique(s):
    # using more space O(n) 
    d = {}
    s =  cleanup(s)
    for i in s:
        if i in d:
            return False
        d[i] = 1
    return True


def is_unique2(s):
    #O(n)time,  space O(n)
    s = cleanup(s)
    return len(s) == len(set(s))

def is_unique3(s):
    #O(n)time,  space O(n)
    s = cleanup(s)
    alpha = 'abcdefghijklmonpqrstuvwxyz'
    for c in s:
        if c in alpha:
            alpha =  alpha.replace(c, "")
        else:
            return False
    return True

print(is_unique("not unique"))
print(is_unique2("ot uniqe"))
print(is_unique3("ot uniqe"))