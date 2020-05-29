class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def find_least_common_ancestor(node_a: Node, node_b: Node, root: Node) -> Node:

    if root is None:
        return None

    if root in (node_a, node_b):
        return root

    search_left = find_least_common_ancestor(node_a, node_b, root.left)
    search_right = find_least_common_ancestor(node_a, node_b, root.right)

    if search_left and search_right:
        return root
    
    return search_left or search_right
