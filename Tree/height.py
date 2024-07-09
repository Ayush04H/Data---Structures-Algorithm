class node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def heights(root):
    if root == None:
        return 0
    lh=heights(root.left)
    rh=heights(root.right)
    return max(lh,rh) + 1

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    print(heights(root))