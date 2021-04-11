##Find the length of string without the len()

def length_str(s):
    if s == '':
        return 0
    return 1 + length_str(s[1:])

print(length_str("1")) 