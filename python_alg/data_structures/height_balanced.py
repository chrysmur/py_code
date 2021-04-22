'''Given the root node of a binary tree, check if its height balanced
A tree is height balanced if for any node, the difference between the right and the left heights is at most 1'''

def is_balanced_bt(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    # first value indicates whether the tree is balanced or not, and if so, the second returns value of the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # unbalanced left subtree
            return BalancedStatusWithHeight(false, 0)
        
        right_result =  check_balanced(tree.right)
        if not right_result.balanced:
            # unbalanced right subtree
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height =  max(left_result, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)