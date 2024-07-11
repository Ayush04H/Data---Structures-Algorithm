from collections import deque
class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def printlevelnode(root):
    if root is None :
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        count= len(q)
        for i in range(count):
            curr=q.popleft()
            print(curr.key,end=" ")
            if curr.left is not None :
                q.append(curr.left)
            if curr.right is not None :
                q.append(curr.right)
        print()

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
    printlevelnode(root)