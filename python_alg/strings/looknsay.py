'''
Given a integer, return the next number in the sequence
1 = 11
11= 21
21 = 1211
1211 = 111221
'''

def looknsay(n):
    if not isinstance(n, int):
        return
    if len(str(n)) == 1:
        return str(1) + str(n)

    result = []
    count = 0
    current = ''
    i = 0
    while i < len(str(n)):
        char = str(n)[i]
        if current == '':
            current = char
        if char == current:
            current = char
            count += 1
        else:
            result.append(str(count)+current)
            current = char
            count = 1            
        i += 1
    result.append(str(count)+current)
    return "".join(result)

# to return the nth number in the series:
#create a function that calls this one n number of times
