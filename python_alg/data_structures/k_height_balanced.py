# Check the height_balanced for more explanation
# The right/left trees but only have a height difference of a max of k

def k_height_balanced(tree, k):
    BalancedStatusWithHeight =  collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    def is_k_balanced(tree, k):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base case

        left_result = is_k_balanced(tree.left, k)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, left_result.height)

        right_result = is_k_balanced(tree.right, k):
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, right_result.height) # no need for height, its returning False anyway

        is_balanced =  abs(left_result.height -  right_result.height) <= k
        height =  max(right_result.height, left_result.height) + 1
        return BalancedStatusWithHeight(True, height)

