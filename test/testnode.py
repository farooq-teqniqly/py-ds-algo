from typing import Tuple

from bst import Node


def test_node_initialization_str():
    node: Node[str] = Node("foo")
    assert node.value == "foo"


def test_node_initialization_int():
    node: Node[int] = Node(1)
    assert node.value == 1


def test_node_initialization_tuple():
    node: Node[Tuple[int, str, int]] = Node((1, "foo", 2))
    assert node.value == (1, "foo", 2)
