from bst import BstNode


def test_bstnode_initialization():
    node: BstNode[str] = BstNode("foo")
    assert node.value == "foo"
    assert node.left is None
    assert node.right is None
