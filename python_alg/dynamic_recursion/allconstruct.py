'''
Given a target and a word bank array, return all the combinations which can result in the target word
"hello", ["somet", "other", "stuff"] > return []
"" , ["somet", "other", "stuff"] => [[]]
'''

def allconstructs(target, wordbank, store={}):
    if target in store: return store[target]
    if target == '': return [[]]
    
    all_ways = []
    for word in wordbank:
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            suffix_ways = allconstructs(suffix, wordbank, store)
            targ_ways = [[word]+[*way] for way in suffix_ways]
            store[target] = targ_ways
            all_ways.extend(targ_ways)
    return all_ways


print(allconstructs("abcdef", ["ab", "abc", "cd",  "def", "abcd"]))
print(allconstructs("purple", ["purp", "p", "ur",  "le", "purpl"]))
print(allconstructs("sabonis", ["is", "bon", "sa",  "onis", "sab"]))
print(allconstructs("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee",  "ee", "eeeef"]))