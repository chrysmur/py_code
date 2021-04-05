'''
Given a string and a word bank, determine if you can construct the string from the words given
canConstruct("abcdef, ["abc", "ac", "def"]) => true
base case = " " return True
'''

def canconstruct(target, wordbank, store={}):
    if target in store: return store[target]
    if target == '':return True
    
    for word in wordbank:
        if word in target and target.index(word) == 0:
            suffix =  target[len(word):]
            result = canconstruct(suffix, wordbank, store)
            store[target] = result
            if result:
                return True

    return False

'''
n = length of target
m = length of wordbank
 Time: O(m^n * n) assuming that all words are matching, we will have to go through the word bank for every char in target
 * m because of the slicing part of the operation, O(n)

 Space: O(m^2) because slicing returns a new string


After memoization
Time: O(n * m^2)
Space: O(m^2)
'''
print(canconstruct("abcdef", ["ab", "abc", "cd",  "def", "abcd"]))
print(canconstruct("sabonis", ["abs", "bon", "sa",  "onis", "abcd"]))
print(canconstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee",  "ee", "eeee"]))
