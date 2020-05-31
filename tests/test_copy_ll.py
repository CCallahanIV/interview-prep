import pytest

from general.microsoft.copy_ll import copy_linked_list, Node


def single_node_ll():
    root = Node(data=3)
    return root


def example_problem():
    root = Node(data=1)
    node_2 = Node(data=2)
    node_3 = Node(data=3)
    node_4 = Node(data=4)
    root.nxt = node_2
    root.other = node_3
    node_2.nxt = node_3
    node_2.other = node_4
    node_3.nxt = node_4
    node_3.other = root
    node_4.other = node_2
    return root


def no_other_pointers():
    root = Node(data=1, nxt=Node(data=2, nxt=Node(data=3)))
    return root


@pytest.mark.parametrize(
    "root",
    [
        pytest.param(
            single_node_ll(),
            id="Single node ll"
        ),
        pytest.param(
            example_problem(),
            id="example problem"
        ),
        pytest.param(
            no_other_pointers(),
            id="Normal linked list - no other pointers"
        ),
    ]
)
def test_is_bst_balanced(root):
    copied_root = copy_linked_list(root)
    curr_original = root
    curr_copied = copied_root
    while curr_original:
        assert curr_copied.data == curr_original.data
        if curr_original.other:
            assert curr_original.other.data == curr_copied.other.data
        curr_original = curr_original.nxt
        curr_copied = curr_copied.nxt
        if curr_original is None:
            assert curr_copied is None
            break        
