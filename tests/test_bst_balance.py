import pytest

from general.microsoft.bst_balance import is_bst_balanced, Node

def build_test_tree_1():
    """Null check"""
    return None

def build_test_tree_2():
    """Single node."""
    root = Node()
    return root

def build_test_tree_3():
    """Simple balanced tree (one node to left)."""
    root = Node()
    root.left = Node()
    return root

def build_test_tree_4():
    """Simple balanced tree one node each side."""
    root = Node()
    root.left = Node()
    root.right = Node()
    return root

def build_test_tree_5():
    """Example tree."""
    root = Node()
    root.left = Node()
    root.left.left = Node()
    root.left.right = Node()
    root.left.right.left = Node()
    root.right = Node()
    root.right.right = Node()
    return root

def build_test_tree_unbalanced_1():
    """Simple example of unbalanced BST."""
    root = Node()
    root.right = Node()
    root.right.right = Node()
    return root

def build_test_tree_unbalanced_2():
    """More complex example of unbalanced BST."""
    root = Node()
    root.right = Node()
    root.left = Node()
    root.left.left = Node()
    root.left.left.right = Node()
    return root


@pytest.mark.parametrize(
    "tree,exp",
    [
        pytest.param(
            build_test_tree_1(),
            True,
            id="Null Check"
        ),
        (
            build_test_tree_2(),
            True
        ),
        (
            build_test_tree_3(),
            True
        ),
        (
            build_test_tree_4(),
            True
        ),
        (
            build_test_tree_5(),
            True
        ),
        (
            build_test_tree_unbalanced_1(),
            False
        ),
        (
            build_test_tree_unbalanced_2(),
            False
        )
    ]
)
def test_is_bst_balanced(tree, exp):
    assert is_bst_balanced(tree) is exp
