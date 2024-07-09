from collections import deque

class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def print_level_order(root):
    if root ==None:
        return
    q=deque()
    q.append(root)
    while len(q)>0:
        node=q.popleft()
        print(node.key,end=" ")
        if node.left!=None:
            q.append(node.left)
        if node.right!=None:
            q.append(node.right)


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