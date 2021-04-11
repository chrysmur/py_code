'''
Given a string, count the number of consonants
AdDbGtePnG
'''

vowel = 'aeiou'

def count_consonants1(s):
    count = 0
    for index in range(len(s)):
        if s[index].lower() not in vowel:
            count += 1

    return count

def count_consonants2(s):
    # base case
    if s == '':
        return 0
    if s[0].lower() not in vowel and s[0].isalpha():
        return 1 + count_consonants2(s[1:])
    else:
        return count_consonants2(s[1:])

    
print(count_consonants1("AdDbGtePnG"))


