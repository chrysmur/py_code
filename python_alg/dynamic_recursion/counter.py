'''
s = "heello"
1: d={h:1}, max_rep = h
2: d={h:1, e:1}, max_rep = h
3: d={h:1, e:2}, max_rep = e
4: d= {h:1, e:2, l:1} max_rep = e
return max_rep, d[max_rep]
'''
def counter(s):
    if len(s) < 2:
        return None
    
    max_char = None
    max_count = 0
    for char in s.replace(' ', ''):
        if char == max_char:
            max_count += 1
        else:
            if max_char and max_count > 1:
                return max_char, max_count
            max_char = char
            max_count = 1
    return None

print(counter("asdf")) # None
print(counter("heeello")) # e, 3
print(counter("hello")) # l, 2
print(counter("my name is chhrys")) # h, 2