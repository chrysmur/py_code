'''
Return how many ways we can construct the target from the given words
'''

def countconstruct(target, wordbank, store={}):
    if target in store: return store[target]
    if target == '': return 1

    total_count = 0
    for word in wordbank:
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            countways_suffix = countconstruct(suffix, wordbank, store)
            store[target] = countways_suffix
            total_count += countways_suffix
    return total_count

print(countconstruct("abcdef", ["ab", "abc", "cd",  "def", "abcd"]))
print(countconstruct("purple", ["purp", "p", "ur",  "le", "purpl"]))
print(countconstruct("sabonis", ["abs", "bon", "sa",  "onis", "abcd"]))
print(countconstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee",  "ee", "eeeef"]))