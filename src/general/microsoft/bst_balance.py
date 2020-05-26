
class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def is_bst_balanced(root: Node) -> bool:
    return (get_depth_of_subtree) > -1


def get_depth_of_subtree(root: Node) -> int:
    if root is None: return 0

    depth_left = get_depth_of_subtree(root.left)
    depth_right = get_depth_of_subtree(root.right)

    if depth_left == -1 or depth_right == -1:
        # Passing along notice of imbalance
        return -1
    
    if abs(depth_left - depth_right) > 1:
        # THIS tree is imbalanced, pass it along
        return -1
    
    return max(depth_left, depth_right) + 1
