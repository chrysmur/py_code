#Implementation

class Node:
    def  __init__(self, value=None):
        self.value = value
        self.left =  None
        self.right = None


#create a stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)

#Creating a queue
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BST:
    def __init__(self):
        self.root = Node()

    def insert(self, value):
        currentNode = self.root
        newNode = Node(value)
        if not currentNode.value:
            currentNode.value = value
        else:
            while currentNode:
                if value < currentNode.value:
                    if not currentNode.left:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if not currentNode.right:
                        currentNode.right = newNode
                        break
                    else:
                        currentNode = currentNode.right
    
    def find(self, value):
        currentNode = self.root
        while currentNode:
            if currentNode.value == value:
                return True
            if currentNode.value > value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

    def preorderT(self, start, traversal=None):
        '''Root, left right '''
        # we can return traversal if we are appending the values to it
        if start:
            print(start.value)
            traversal = self.preorderT(start.left, traversal)
            traversal = self.preorderT(start.right, traversal)

    def inorderT(self, start, traversal=None):
        if start:
            traversal = self.postorderT(start.left)
            print(start.value)
            traversal = self.postorderT(start.right, traversal)

    def postorderT(self, start, traversal=None):
        if start:
            traversal = self.postorderT(start.left, traversal)
            traversal = self.postorderT(start.right, traversal)
            print(start.value)

    def level_orderT(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        
        while len(queue) > 0:
            print(queue.peek().value)
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def level_listT(self, start):
        ''' All values on the same level should be printed horizontally '''
        if start is None:
            return
        # use queue to track all values
        queue = Queue()
        cur_level = 1
        start.level = cur_level
        traversal = ""
        # append the first value to que
        queue.enqueue(start)
        while len(queue) > 0:
            # Dequeue a node to handle it
            node = queue.dequeue() 
            #Check if the current node has the same value as the cur_level, see if you need to add a new line
            if node.level > cur_level:
                traversal += "\n"
                cur_level += 1 # increment the level because the current value is a level lower than the current_level held
            traversal +=str(node.value) + " "
            if node.left:
                nextnode = node.left
                nextnode.level = cur_level + 1
                queue.enqueue(nextnode)
            if node.right:
                nextnode = node.right
                nextnode.level = cur_level + 1
                queue.enqueue(nextnode)
        return traversal

    def height(self, start):
        if start is None:
            return -1
        left =  self.height(start.left)
        right = self.height(start.right)
        
        return 1 + max(left, right)

    def reversal_level_orderT(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.right)

        while len(stack) > 0:
            node = stack.pop()
            print(node.value)

    
    def size(self, start):
        # the size is the number of all nodes
        if start is None:
            return
        stack = Stack()
        stack.push(self.root)

        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size







bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
# bst.level_orderT(bst.root)
# print(bst.height(bst.root))
# print(bst.level_listT(bst.root))
print(bst.size(bst.root))


