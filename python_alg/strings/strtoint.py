'''
given a string, convert it to int
'''

def str_to_int(s):
    output = 0
    if s[0] == '-':
        start = 1
        is_negative = True
    else:
        start = 0
        is_negative = False

    for i, val in enumerate(s[start:][::-1]):
        value = (ord(val) - ord('0')) * 10 ** i 
        output += value

    if is_negative:
        return -1 * output
    return output

print(str_to_int('-290'))