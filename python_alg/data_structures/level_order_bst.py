'''
Given a binary tree, return an array consisting of the keys at the same level. Keys should appear
in the order of the corresponding nodes’ depths, breaking ties from left to right
'''
# we use queue of nodes to store nodes at depth i and a queue of nodes at depth i+1
# we process nodes at i, then proceed to i+1...

def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree])

    while curr_depth_nodes:
        next_depth_nodes, this_level =  collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes =  next_depth_nodes
    return result 
        
