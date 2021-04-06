def anagram1(s1, s2):
    s1 = s1.replace(" ",  "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2) #O(nlogn)


def anagram2(s1, s2):
    ht = dict()
    if len(s1) != len(s2):
        return False
    for i in s1: #O(n)
        ht[i] = ht.get(i, 0) + 1
    
    for i in s2: #O(m)
        ht[i] =  ht.get(i,0) - 1

    for i, val in ht.items(): #O(k)
        if val != 0:
            return False
    
    return True


print(anagram2("fairy tales", "rail safetyx"))
