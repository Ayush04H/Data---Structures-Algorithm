import math
class node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.key=key


def max_node(root):
    if root==None:
        return -math.inf
    else:
        lm=max_node(root.left)
        rm=max_node(root.right)
        return max(root.key,lm,rm)
    

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
    print(max_node(root))