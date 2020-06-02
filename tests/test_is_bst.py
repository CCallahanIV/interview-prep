import pytest

from general.microsoft.is_bst import is_bst, Node

def single_node():
    root = Node(4)
    return root


def simple_not_bst():
    root = Node(
        10,
        right=Node(5)
    )
    return root


def example_problem():
    root = Node(
        10,
        left=Node(
            7,
            left=Node(3),
            right=Node(8)
        ),
        right=Node(
            15,
            left=Node(9),
            right=Node(17)
        )
    )
    return root


def example_problem_but_true():
    root = Node(
        10,
        left=Node(
            7,
            left=Node(3),
            right=Node(8)
        ),
        right=Node(
            15,
            left=Node(11),
            right=Node(17)
        )
    )
    return root


@pytest.mark.parametrize(
    "root,exp",
    [
        pytest.param(
            single_node(),
            True,
            id="Single node bst"
        ),
        pytest.param(
            simple_not_bst(),
            False,
            id="example problem"
        ),
        pytest.param(
            example_problem(),
            False,
            id="Example tree from problem definition."
        ),
        pytest.param(
            example_problem_but_true(),
            True,
            id="Example BST that is a BST."
        )
    ]
)
def test_is_bst_balanced(root,exp):
    assert is_bst(root) is exp
