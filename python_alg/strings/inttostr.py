'''
convert an integer to string without using the str method

'''

def int_to_str(integer):
     # check if its negative
    if integer < 0:
        is_negative = True
        integer *= -1
    else:
        is_negative = False

    output_str = []
    while integer > 0:
        output_str.append(chr(ord('0') + integer % 10)) # get the ascii of 0 then add  the remainder of int/10 then append it 
        integer //= 10
    output_str = ''.join(output_str[::-1])
    if is_negative:
        return "-" + output_str
    else:
        return output_str

print(int_to_str(-101))