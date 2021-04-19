class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LL:
    def __init__(self, data=None):
        self.head = Node(data)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head =  new_node

        else:
            cur = self.head
            while cur.next:
                prev =  cur
                cur = cur.next
                
            new_node.prev  = cur
            cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node        
            self.head = new_node
       
    def print_nodes(self):
        if not self.head:
            print(None)
            return
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur =  cur.next


ll = LL()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
print()
ll.print_nodes()