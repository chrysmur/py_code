'''
Given a number of people N and an array of integers, each one representing the amount of people a type of umbrella can handle, output the minimum number of umbrellas needed to handle N people.

No umbrella could have left spaces. Which means if a umbrella can handle 2 people, there should be 2 people under it.

If there's no solution, return -1.

'''

def umbrella_count(people, umbrellas):
    if people < 0: return None
    if people == 0: return []

    shortest = None

    for umb in umbrellas:
        remainder =  people  -  umb
        result =  umbrella_count(remainder, umbrellas)
        if result is not None:
            combination =[*result, umb]
            if not shortest or (len(shortest) > len(combination)):
                shortest = combination

    return shortest

def solution(people, umbrellas):
    count = umbrella_count(people, umbrellas)
    if count: return len(count);  
    else: return  -1


print(solution(10, []))

