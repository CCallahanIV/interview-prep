from math import inf

# Assumptions:
#  - Does not need to `balanced` to be considered a BST
#  - no duplicate values

class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_bst(root: Node, lower_bound: int = -inf, upper_bound: int = inf) -> bool:
    if root.data < lower_bound or root.data > upper_bound:
        return False
    
    is_bst_left, is_bst_right = True, True
    if root.left:
        is_bst_left = is_bst(root.left, lower_bound, root.data)
    
    if root.right:
        is_bst_right = is_bst(root.right, root.data, upper_bound)

    return is_bst_left and is_bst_right
