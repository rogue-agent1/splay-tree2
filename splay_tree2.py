#!/usr/bin/env python3
"""Splay tree — self-adjusting BST with amortized O(log n)."""
import sys

class Node:
    def __init__(self, key):
        self.key = key; self.left = self.right = self.parent = None

class SplayTree:
    def __init__(self): self.root = None
    def _rot_r(self, x):
        y = x.left; x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y
    def _rot_l(self, x):
        y = x.right; x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left: self._rot_r(x.parent)
                else: self._rot_l(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._rot_r(x.parent.parent); self._rot_r(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._rot_l(x.parent.parent); self._rot_l(x.parent)
            elif x == x.parent.right:
                self._rot_l(x.parent); self._rot_r(x.parent)
            else:
                self._rot_r(x.parent); self._rot_l(x.parent)
    def insert(self, key):
        n = Node(key); y = None; x = self.root
        while x: y = x; x = x.left if key < x.key else x.right
        n.parent = y
        if not y: self.root = n
        elif key < y.key: y.left = n
        else: y.right = n
        self._splay(n)
    def search(self, key):
        x = self.root
        while x:
            if key == x.key: self._splay(x); return True
            x = x.left if key < x.key else x.right
        return False
    def inorder(self):
        res, stack, n = [], [], self.root
        while stack or n:
            while n: stack.append(n); n = n.left
            n = stack.pop(); res.append(n.key); n = n.right
        return res

def main():
    st = SplayTree()
    for x in [10,5,15,3,7,12,20]: st.insert(x)
    print(f"Inorder: {st.inorder()}")
    st.search(7); print(f"Root after search(7): {st.root.key}")

if __name__ == "__main__": main()
