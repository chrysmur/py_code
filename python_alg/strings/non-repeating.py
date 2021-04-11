def firstNonRepeatingCharacter(string):
    # Write your code here.
	string_dict = dict()
	for index, char in enumerate(string):
		string_dict[index] = string_dict.get(char, 0) + 1

	lowest_index = len(string)
    for key, value in string_dict.items():
        
        if value == 1:
            lowest_index = min(lowest_index, key)
    if lowest_index == len(string):
		return -1
	return lowest_index


print(firstNonRepeatingCharacter('abcdcaf'))
