import argparse

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class SplayTree:
    def __init__(self): self.root = None
    def _right_rotate(self, x):
        y = x.left; x.left = y.right; y.right = x; return y
    def _left_rotate(self, x):
        y = x.right; x.right = y.left; y.left = x; return y
    def _splay(self, root, key):
        if not root or root.key == key: return root
        if key < root.key:
            if not root.left: return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right: root.left = self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root
        else:
            if not root.right: return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left: root.right = self._right_rotate(root.right)
            return self._left_rotate(root) if root.right else root
    def insert(self, key):
        if not self.root: self.root = Node(key); return
        self.root = self._splay(self.root, key)
        if self.root.key == key: return
        n = Node(key)
        if key < self.root.key: n.right = self.root; n.left = self.root.left; self.root.left = None
        else: n.left = self.root; n.right = self.root.right; self.root.right = None
        self.root = n
    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root and self.root.key == key
    def inorder(self):
        result = []
        def io(n):
            if not n: return
            io(n.left); result.append(n.key); io(n.right)
        io(self.root); return result

def main():
    p = argparse.ArgumentParser(description="Splay tree")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        st = SplayTree()
        for v in [10, 20, 30, 40, 50, 25]: st.insert(v)
        print(f"Inorder: {st.inorder()}")
        print(f"Search 30: {st.search(30)}")
        print(f"Root after splay: {st.root.key}")
    else: p.print_help()

if __name__ == "__main__":
    main()
