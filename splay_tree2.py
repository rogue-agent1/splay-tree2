#!/usr/bin/env python3
"""Splay Tree — self-adjusting BST with amortized O(log n) operations."""

class Node:
    __slots__ = ('key', 'val', 'left', 'right', 'parent')
    def __init__(self, key, val=None):
        self.key, self.val = key, val
        self.left = self.right = self.parent = None

class SplayTree:
    def __init__(self): self.root = None; self.size = 0
    
    def _rotate_left(self, x):
        y = x.right; x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    
    def _rotate_right(self, x):
        y = x.left; x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y
    
    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left: self._rotate_right(x.parent)
                else: self._rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._rotate_right(x.parent.parent); self._rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._rotate_left(x.parent.parent); self._rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self._rotate_left(x.parent); self._rotate_right(x.parent)
            else:
                self._rotate_right(x.parent); self._rotate_left(x.parent)
    
    def insert(self, key, val=None):
        if not self.root: self.root = Node(key, val); self.size += 1; return
        node = self.root; parent = None
        while node:
            parent = node
            if key < node.key: node = node.left
            elif key > node.key: node = node.right
            else: node.val = val; self._splay(node); return
        new = Node(key, val); new.parent = parent
        if key < parent.key: parent.left = new
        else: parent.right = new
        self._splay(new); self.size += 1
    
    def find(self, key):
        node = self.root
        while node:
            if key < node.key: node = node.left
            elif key > node.key: node = node.right
            else: self._splay(node); return node.val
        return None
    
    def inorder(self):
        result = []; stack = []; node = self.root
        while stack or node:
            while node: stack.append(node); node = node.left
            node = stack.pop(); result.append((node.key, node.val)); node = node.right
        return result

if __name__ == "__main__":
    st = SplayTree()
    for k in [5, 3, 7, 1, 4, 6, 8, 2]: st.insert(k, f"v{k}")
    print(f"Find 4: {st.find(4)} (root now: {st.root.key})")
    print(f"Find 7: {st.find(7)} (root now: {st.root.key})")
    print(f"Inorder: {st.inorder()}")
