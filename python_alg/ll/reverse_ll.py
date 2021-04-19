class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self, data = None):
        self.head = Node(data)

    def append(self, value):
        new_node = Node(value)
        current_node  = self.head
        while current_node.next:
            current_node =  current_node.next

        current_node.next = new_node

    def reverse(self):
        current_node =  self.head
        prev = None
        while current_node:
            next_node =  current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head =  prev

    def print_nodes(self):
        if not self.head:
            print(None)
            return
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur =  cur.next

ll = LL(1)
ll.append(2)
ll.append(3)
ll.print_nodes()
print("\n")
ll.reverse()
ll.print_nodes()