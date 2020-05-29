import pytest

from general.microsoft.bt_least_common_ancestor import find_least_common_ancestor, Node


def build_sample_tree():
    root = Node(
        left=Node(
            left=Node(
                left=Node(),
                right=Node()
            ),
            right=Node()
        ),
        right=Node(
            left=Node(),
            right=Node()
        )
    )
    node_a = root.left.left.right
    node_b = root.left.right
    exp_node = root.left
    return node_a, node_b, root, exp_node


def simple_tree():
    root = Node(
        left=Node(),
        right=Node()
    )
    node_a = root.left
    node_b = root.right
    exp_node = root
    return node_a, node_b, root, exp_node


@pytest.mark.parametrize(
    "node_a,node_b,root,exp_node",
    [
        pytest.param(
            *build_sample_tree(),
            id="Example from problem definition"
        ),
        pytest.param(
            *build_sample_tree(),
            id="Simple tree, root node is LCA"
        ),
    ]
)
def test_is_bst_balanced(node_a, node_b, root, exp_node):
    assert find_least_common_ancestor(node_a, node_b, root) is exp_node
