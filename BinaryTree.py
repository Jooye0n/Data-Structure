"""Stand-alone binary tree class"""


class BinaryTree:
    class _Node:
        def __init__(self, e, p, l, r):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r

        def __repr__(self):
            return self._element

        def __str__(self):
            return str(self._element)

        def element(self):
            return self._element

        def parent(self):
            return self._parent

        def left(self):
            return self._left

        def right(self):
            return self._right

        def set_element(self, e):
            self._element = e

        def set_parent(self, p):
            self._parent = p

        def set_left(self, l):
            self._left = l

        def set_right(self, r):
            self._right = r

    def __init__(self, root=None):
        self._root = root

    def _subtree_len(self, p):
        if p is None:
            return 0
        else:
            return 1 + self._subtree_len(p.left()) + self._subtree_len(p.right())

    def __len__(self):
        return self._subtree_len(self.root())

    def _subtree_str(self, p):
        if p is None:
            return '[]'
        elif self.is_external(p):
            return f'[{str(p)}]'
        else:
            return f'[{str(p)} {str(self._subtree_str(p.left()))} {str(self._subtree_str(p.right()))}]'

    def __str__(self):
        return self._subtree_str(self.root())

    def root(self):
        return self._root

    def set_root(self, root):
        self._root = root

    def is_root(self, p):
        return p == self._root

    def is_external(self, p):
        return not self.is_internal(p)

    def is_internal(self, p):
        return True if p.left() or p.right() else False

    def is_empty(self):
        return self._root is None

    def children(self, p):
        if p.left():
            yield p.left()

        if p.right():
            yield p.right()

    def num_children(self, p):
        count = 0
        for c in self.children(p):
            count += 1
        return count

    def depth(self, p):
        if self.is_root(p):
            return 1
        else:
            return 1 + self.depth(p.parent())

    def _height(self, p):
        if self.is_external(p):
            return 1
        else:
            return 1 + max([self._height(c) for c in self.children(p)])

    def height(self):
        if self.is_empty():
            return 0
        else:
            return self._height(self.root())

    def _attach(self, p, t1, t2):
        """Attach binary trees t1 and t2, respectively, as the left and right subtrees of the external node p."""
        if self.is_internal(p):  # p should be external
            raise AttributeError(f"{p} should be external")

        if not t1.is_empty():  # attached t1 as left subtree of node
            t1.root().set_parent(p)
            p.set_left(t1.root())
            t1.set_root(None)  # set t1 empty
        if not t2.is_empty():  # attached t2 as right subtree of node
            t2.root().set_parent(p)
            p.set_right(t2.root())
            t2.set_root(None)  # set t2 instance to empty

    def add_root(self, element):
        """Add a node of element at root"""
        new_node = self._Node(element, None, self.root(), None)
        if self._root:
            self._root._parent = new_node
        self._root = new_node
        return new_node

    def add_child(self, p, element):
        """Add a node of element as the child of p"""
        if not p.left():
            return self.add_left(p, element)
        elif not p.right():
            return self.add_right(p, element)
        else:
            raise OverflowError(f"{self}.{p} is already full of children {p.left()} {p.right}.")

    def add_left(self, p, element):
        new_node = self._Node(element, p, None, None)
        if p.left():
            raise AttributeError(f"{self}.{p} has already left child {p.left()}")
        else:
            p.set_left(new_node)
            return new_node

    def add_right(self, p, element):
        new_node = self._Node(element, p, None, None)
        if p.right():
            raise AttributeError(f"{self}.{p} has already right child {p.right()}")
        else:
            p.set_right(new_node)
            return new_node

    def _subtree_inorder(self, p):
        if p.left():
            for other in self._subtree_inorder(p.left()):
                yield other
        yield p
        if p.right():
            for other in self._subtree_inorder(p.right()):
                yield other

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_level_order(self, p):
        queue = list()  # queue simulates Queue data structures
        queue.append(p)
        while len(queue) != 0:
            p = queue.pop(0)
            yield p
            for c in self.children(p):
                queue.append(c)

    def level_order(self):
        if not self.is_empty():
            for p in self._subtree_level_order(self.root()):
                yield p

    def inorder_prev(self, p):
        if p.left():
            walk = p.left()
            while walk.right() is not None:
                walk = walk.right()
            return walk
        else:
            walk = p
            above = walk.parent()
            while above is not None and walk is above.left():
                walk = above
                above = walk.parent()
            return above

    def inorder_next(self, p):
        if p.right():
            walk = p.right()
            while walk.left() is not None:
                walk = walk.left()
            return walk
        else:
            walk = p
            above = walk.parent()
            while above is not None and walk is above.right():
                walk = above
                above = walk.parent()
            return above

    def preorder_prev(self, p):
        above = p.parent()
        if above:
            if p is above.right() and above.left():
                walk = above.left()
                while self.is_internal(walk):
                    if walk.right():
                        walk = walk.right()
                    else:
                        walk = walk.left()
                return walk
        return above

    def preorder_next(self, p):
        if self.is_external(p):
            walk = p
            above = p.parent()
            while walk is not above.left() or above.right() is None:
                walk = above
                above = walk.parent()
                if above is None:
                    return None
            return above.right()
        else:
            return p.left() if p.left() else p.right()

    def postorder_prev(self, p):
        if self.is_external(p):
            walk = p
            above = p.parent()
            while walk is not above.right() or above.left() is None:
                walk = above
                above = walk.parent()
                if above is None:
                    return None
            return above.left()
        else:
            return p.right() if p.right() else p.left()

    def postorder_next(self, p):
        above = p.parent()
        if above:
            if p is above.left() and above.right():
                walk = above.right()
                while self.is_internal(walk):
                    if walk.left():
                        walk = walk.left()
                    else:
                        walk = walk.right()
                return walk
        return above


if __name__ == "__main__":
    T = BinaryTree()
    root = A = T.add_root("A")
    B = T.add_left(T.root(), "B")
    C = T.add_right(T.root(), "C")
    D = T.add_child(T.root().left(), "D")
    E = T.add_child(T.root().left(), "E")
    F = T.add_child(T.root().right(), "F")
    G = T.add_child(T.root().right(), "G")
    H = T.add_child(T.root().right().left(), "H")
    I = T.add_right(T.root().right().right(), "I")
    print(f'{T}: height {T.height()}, size {len(T)}')

    print("Inorder Traversal: ", end='')
    for pos in T.inorder():
        print(pos, end=' ')
    print('', end='\n')

    print("Inorder Traversal: ", end='')
    for pos in T.inorder():
        p = T.inorder_prev(pos)
        n = T.inorder_next(pos)
        print(p.element() if p else None, pos.element(), n.element() if n else None, end=" / ")
    print('', end='\n')

    print("Preorder Traversal: ", end='')
    for pos in T.preorder():
        print(pos.element(), end=" ")
    print('', end='\n')

    print("Preorder Traversal: ", end='')
    for pos in T.preorder():
        p = T.preorder_prev(pos)
        n = T.preorder_next(pos)
        print(p.element() if p else None, pos.element(), n.element() if n else None, end=" / ")
    print('', end='\n')

    print("Postorder Traversal: ", end='')
    for pos in T.postorder():
        print(pos.element(), end=" ")
    print('', end='\n')

    print("Postorder Traversal: ", end='')
    for pos in T.postorder():
        p = T.postorder_prev(pos)
        n = T.postorder_next(pos)
        print(p.element() if p else None, pos.element(), n.element() if n else None, end=" / ")
    print('', end='\n')

    print("Levelorder Traversal: ", end='')
    for p in T.level_order():
        print(p.element(), end=" ")
        last = p
    print('', end='\n')
    print("The last node is ", last.element())



