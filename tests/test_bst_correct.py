import pytest

from general.microsoft.bst_correct import repair_bst, in_order_traverse, Node


def build_sample_tree():
    root = Node(
        data=7,
        left=Node(
            data=5,
            left=Node(
                data=4
            ),
            right=Node(
                data=6
            )
        ),
        right=Node(
            data=8
        )
    )
    return root


def build_swapped_tree():
    root = Node(
        data=7,
        left=Node(
            data=5,
            left=Node(
                data=8
            ),
            right=Node(
                data=6
            )
        ),
        right=Node(
            data=4
        )
    )
    return root


@pytest.mark.parametrize(
    "correct_tree,swapped_tree",
    [
        pytest.param(
            build_sample_tree(),
            build_swapped_tree(),
            id="Simple swapped example"
        ),
    ]
)
def test_is_bst_balanced(correct_tree, swapped_tree):
    correct_in_order = [
        node.data for node in in_order_traverse(correct_tree)
    ]
    swapped_in_order = [
        node.data for node in in_order_traverse(swapped_tree)
    ]
    assert correct_in_order != swapped_in_order
    repaired_tree = repair_bst(swapped_tree)
    repaired_in_order = [
        node.data for node in in_order_traverse(repaired_tree)
    ]
    assert correct_in_order == repaired_in_order
