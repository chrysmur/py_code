'''
Find if the string given is a palindrome
Ignore punctuations

'''
#solution 1
def palindrome1(s):
    #O(N) space
    clean_s = ''.join([char for char in s.replace(" ", "").lower() if char.isalnum()])
    return clean_s == clean_s[::-1]

def palindrome2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
    return True

print(palindrome1("was it a cat ...i saw?"))
