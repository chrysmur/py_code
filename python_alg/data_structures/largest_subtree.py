# Given a tree, return the largest subtree that is complete

def largest_subtree(tree):
    LargestStatusTree = collections.namedtuple(
        "LargestStatusTree", ('balanced', 'height')
    )
    def is_largest(tree):
        if not tree:
            return LargestStatusTree(True, -1)

        left_result = is_largest(tree.left)
        if not left_result.balanced:
            return LargestStatusTree(False, 0)
        
        right_result =  is_largest(tree.right)
        if not right_result:
            return LargestStatusTree(False, 0)

        is_balanced =  abs(right_result.height - left_result.height) <= 1
        height =  max(right_result.height, left_result.height) + 1
        return LargestStatusTree(True, height)
    return is_largest(tree).height