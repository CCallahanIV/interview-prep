class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Assumptions:
#   1. the given node is the root node of a BST that was valid before being swapped.
#   2. only two nodes were swapped.


def swap_data_for_nodes(node_1, node_2):
    node_1.data, node_2.data = node_2.data, node_1.data


def in_order_traverse(root: Node) -> Node:
    """Will yield nodes in in-order order."""
    if root.left: yield from in_order_traverse(root.left)
    yield root
    if root.right: yield from in_order_traverse(root.right)


def repair_bst(root: Node) -> Node:
    # 1. Produce the in-order traversal of the tree for the given root Node as a list of nodes
    in_order_nodes = [
        node for node in in_order_traverse(root)
    ]
    # 2. Find where in the list, there is a discontinuity (not sorted order)
    disconinuity_idxes = []
    for i in range(len(in_order_nodes) - 1):
        if in_order_nodes[i].data > in_order_nodes[i + 1].data:
            disconinuity_idxes.append(i)
    
    if not disconinuity_idxes:
        # in-order traversal checked out, we're good.
        return root
    
    # 3. If two discontinuities: swap first node of first node of first discontinuity with second node
    #    of second disconituity
    idx_to_swap_1 = None
    idx_to_swap_2 = None
    if len(disconinuity_idxes) == 2:
        idx_to_swap_1 = disconinuity_idxes[0]
        idx_to_swap_2 = disconinuity_idxes[1] + 1

    if len(disconinuity_idxes) == 1:
        idx_to_swap_1 = disconinuity_idxes[0]
        idx_to_swap_2 = disconinuity_idxes[0] + 1

    swap_data_for_nodes(in_order_nodes[idx_to_swap_1], in_order_nodes[idx_to_swap_2])
    return root

