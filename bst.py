from typing import TypeVar, Generic, Optional, Callable

TNode = TypeVar("TNode")


class Node(Generic[TNode]):
    def __init__(self, val: TNode):
        self._value = val

    @property
    def value(self):
        return self._value


class BstNode(Node[TNode]):
    def __init__(self, val: TNode):
        super().__init__(val)
        self._left: Optional[BstNode] = None
        self._right: Optional[BstNode] = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        self._left = val

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        self._right = val


class Bst(Generic[TNode]):
    def __init__(self):
        self._root = None

    @property
    def root(self) -> BstNode[TNode]:
        return self._root

    def search(self, val: TNode, cb: Callable[[TNode], None]):
        if self._root is None:
            cb(None)
        else:
            self._search(val, self._root, cb)

    def _search(self, val: TNode, current: BstNode[TNode], cb: Callable[[TNode], None]):
        if val < current.value:
            if current.left is None:
                cb(None)
            else:
                self._search(val, current.left, cb)
        elif val > current.value:
            if current.right is None:
                cb(None)
            else:
                self._search(val, current.right, cb)
        else:
            cb(val)

    def insert(self, val: TNode):
        if self._root is None:
            self._root = BstNode(val)
        else:
            self._insert(val, self._root)

    def _insert(self, val: TNode, current: BstNode[TNode]):
        if val < current.value:
            if current.left is None:
                current.left = BstNode(val)
            else:
                self._insert(val, current.left)
        else:
            if current.right is None:
                current.right = BstNode(val)
            else:
                self._insert(val, current.right)

    def in_order(self, cb: Callable[[TNode], None]):
        self._in_order(self._root, cb)

    def _in_order(self, current: BstNode[TNode], cb: Callable[[TNode], None]):
        if current is not None:
            self._in_order(current.left, cb)
            cb(current.value)
            self._in_order(current.right, cb)
