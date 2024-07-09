class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def treesize(root):
    if root==None:
        return 0
    else:
        ls=treesize(root.left)
        rs=treesize(root.right)
        return ls+rs+1

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

    print("Tree Size\n")
    sz=treesize(root)
    print(sz)