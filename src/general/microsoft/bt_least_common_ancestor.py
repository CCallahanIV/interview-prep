class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def find_least_common_ancestor(node_a: Node, node_b: Node, root: Node) -> Node:

    if root is None:
        # Base case - I'm a leaf or a there is no root.
        return None

    if root in (node_a, node_b):
        # I am one of the nodes you're looking for, send this knowledge up the tree.
        return root

    # Haven't found a leaf or one of our target nodes, search.

    search_left = find_least_common_ancestor(node_a, node_b, root.left)
    search_right = find_least_common_ancestor(node_a, node_b, root.right)

    # Search results show that the current root IS the LCA, return it
    if search_left and search_right:
        return root

    # We've made it to the top, return search result that is the LCA
    return search_left or search_right
