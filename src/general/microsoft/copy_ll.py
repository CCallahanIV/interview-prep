class Node:
    def __init__(self, data=None, nxt=None, other=None):
        self.data = data
        self.nxt = nxt
        self.other = other


def copy_linked_list(root: Node) -> Node:
    """
    This solution should run in O(N) time. We run through the original linked list twice, once to copy
    data to a set of new nodes and create a mapping of old to new node.

    Then a second time to shift the nxt and other pointers using the list.

    This requires O(N) extra space as we store not only a copy of the new nodes, but a mapping of old to new.
    """
    curr_original_node = root
    original_to_copy_node_map = {}
    while curr_original_node:
        # O(N) where N is number of nodes
        new_node = Node(
            data=curr_original_node.data,
            nxt=curr_original_node.nxt,
            other=curr_original_node.other
        )
        original_to_copy_node_map[curr_original_node] = new_node
        curr_original_node = curr_original_node.nxt

    curr_original_node = root
    while curr_original_node:
        # O(N) where N is number of nodes
        new_node = original_to_copy_node_map[curr_original_node]
        if new_node.nxt:
            new_node.nxt = original_to_copy_node_map[curr_original_node.nxt]
        if new_node.other:
            new_node.other = original_to_copy_node_map[curr_original_node.other]
        curr_original_node = curr_original_node.nxt
        
    return original_to_copy_node_map[root]
