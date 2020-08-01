from typing import List

from bst import Bst


def test_bst_insert():
    bst: Bst[int] = Bst()
    bst.insert(100)
    assert bst.root.value == 100
    assert bst.root.left is None
    assert bst.root.right is None

    bst.insert(50)
    assert bst.root.left.value == 50
    assert bst.root.right is None

    bst.insert(150)
    assert bst.root.right.value == 150

    bst.insert(25)
    assert bst.root.left.left.value == 25

    bst.insert(200)
    assert bst.root.right.right.value == 200

    bst.insert(75)
    assert bst.root.left.right.value == 75

    bst.insert(125)
    assert bst.root.right.left.value == 125


def test_bst_in_order():
    values = [100, 50, 25, 150, 125, 200]
    bst: Bst[int] = Bst()

    for value in values:
        bst.insert(value)

    nodes: List[int] = []
    bst.in_order(lambda val: nodes.append(val))

    assert nodes == sorted(values)


def test_search_when_root_is_null():
    bst = Bst()
    result = 1

    def cb(val):
        nonlocal result
        result = val

    bst.search(100, cb)

    assert result is None


def test_search():
    values = [100, 50, 25, 150, 125, 200]
    bst: Bst[int] = Bst()

    for value in values:
        bst.insert(value)

    search_results: List[bool] = []

    def cb(val: int):
        if val is not None:
            search_results.append(True)
        else:
            search_results.append(False)

    bst.search(150, cb)
    bst.search(300, cb)

    assert search_results == [True, False]
