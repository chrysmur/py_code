'''
In this recursion problem:
We want to move n disks from A to C via B
We move values n-1 values from A to B then remaining from A to C
Then we use A as the Via to move the remaining values from  B to C
'''
def move(_from, to):
    print(f"Move from ${_from} to ${to}")

def hanoi(disks, _from, via, to):
    if disks == 0:
        return
    hanoi(disks-1, _from, to, via)
    move(_from, to)
    hanoi(disks-1, via, _from, to)


hanoi(4, 'A', 'B', 'C')