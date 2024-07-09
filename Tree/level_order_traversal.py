from height import heights  # importing height.py
from print_kth_node import print_nth_node

class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def print_level_order(root):
    h=heights(root)
    for k in range(h):
        print_nth_node(root,k)

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.left.right.right=node(7)
    root.left.right.left=node(6)
    root.left.left.right = node(10)
    root.left.left.left = node(20)

    print_level_order(root)