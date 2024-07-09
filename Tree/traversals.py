class node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k
def inorder(root):

    if root != None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)


def preorder(root):

    if root != None:
        preorder(root.left)
        preorder(root.right)
        print(root.key,end=" ")

def postorder(root):

    if root != None:
        print(root.key,end=" ")
        postorder(root.left)
        postorder(root.right)


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

    print("Inorder\n")
    inorder(root)
    print("\n")
    print("Preorder\n")
    preorder(root)
    print("\n")
    print("Postorder\n")
    postorder(root)
    print("\n")