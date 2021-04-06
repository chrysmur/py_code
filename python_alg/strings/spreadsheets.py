'''
Function that receives  a spreadsheet ID and returns its column count
A = 1,
AA = 27
'''
def spreadsheet(id):
    a = ord('A') #65
    score = 0
    for index, al in enumerate(id[::-1]):
        ord_al = ord(al.upper()) + 1
        val = ord_al - a
        score += val * (26**index)

    return score


print(spreadsheet("zz"))





     