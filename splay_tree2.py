#!/usr/bin/env python3
"""Splay Tree — zero-dep."""

class SplayNode:
    def __init__(self, key):
        self.key=key; self.left=self.right=None

class SplayTree:
    def __init__(self): self.root=None
    def _right_rotate(self, x):
        y=x.left; x.left=y.right; y.right=x; return y
    def _left_rotate(self, x):
        y=x.right; x.right=y.left; y.left=x; return y
    def _splay(self, root, key):
        if not root or root.key==key: return root
        if key<root.key:
            if not root.left: return root
            if key<root.left.key:
                root.left.left=self._splay(root.left.left,key)
                root=self._right_rotate(root)
            elif key>root.left.key:
                root.left.right=self._splay(root.left.right,key)
                if root.left.right: root.left=self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root
        else:
            if not root.right: return root
            if key>root.right.key:
                root.right.right=self._splay(root.right.right,key)
                root=self._left_rotate(root)
            elif key<root.right.key:
                root.right.left=self._splay(root.right.left,key)
                if root.right.left: root.right=self._right_rotate(root.right)
            return self._left_rotate(root) if root.right else root
    def insert(self, key):
        if not self.root: self.root=SplayNode(key); return
        self.root=self._splay(self.root,key)
        if self.root.key==key: return
        n=SplayNode(key)
        if key<self.root.key: n.right=self.root; n.left=self.root.left; self.root.left=None
        else: n.left=self.root; n.right=self.root.right; self.root.right=None
        self.root=n
    def search(self, key):
        self.root=self._splay(self.root,key)
        return self.root and self.root.key==key
    def inorder(self):
        result=[]
        def _in(n):
            if n: _in(n.left); result.append(n.key); _in(n.right)
        _in(self.root); return result

if __name__=="__main__":
    st=SplayTree()
    for k in [10,5,15,3,7,12,20]: st.insert(k)
    print(f"Inorder: {st.inorder()}")
    st.search(7)
    print(f"After search(7), root: {st.root.key}")
    st.search(12)
    print(f"After search(12), root: {st.root.key}")
