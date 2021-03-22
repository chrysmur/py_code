#!/usr/bin/python3
'''
A function that receives a string of operations separated by space
if Operation is a number, push it to stack
if it is DUP, push the last value in the stuck again
if  + pop the last two and add them then push then back
if - pop the last two and subtract the second from the first and push result
if result  of - is negative return error (-1)
'''
class Stack:
    def __init__(self):
        self. __operations = []

    def push(self, value):
        self.__operations.append(value)

    def pop(self):
        return self.__operations.pop()

    @property
    def length(self):
        return len(self.__operations)

    def peek(self):
        return self.__operations[-1]

def run_operation(S):
    operations = S.split(' ')
    stack = Stack()

    for op in operations:
        if op == 'POP':
            if stack.length > 0:
                stack.pop()
            else: return -1

        elif op == 'DUP':
            if stack.length > 0:
                stack.push(stack.peek())
            else: return -1

        elif op == "+":
            if stack.length > 2:
                first = int(stack.pop())
                second = int(stack.pop())
                stack.push(first + second)
            else: return -1

        elif op == "-":
            if stack.length >= 2:
                first = int(stack.pop())
                second = int(stack.pop())
                stack.push(first - second)
            else: return -1
        else:
            stack.push(op)
    return stack.peek()

s = "4 5 - DUP"
print(run_operation(s))