class node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def inorder(root):
    s=[]

    if root != None:
        inorder(root.left)
        s.append(root.key)
        inorder(root.right)

    return s

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    s=inorder(root)
    print(s)
