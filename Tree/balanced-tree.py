class node:
    def __init__(self,key):
        self.left=None
        self.right=None 
        self.key=key


def heights(root):
    if root == None:
        return 0
    ls=heights(root.left)
    rs=heights(root.right)
    return max(ls,rs) +1

def isbalanced(root):
    if root == None:
        return True 
    ls=heights(root.left)
    rs=heights(root.right)

    if (abs(ls-rs) <=1 ) and isbalanced(root.left) is True and isbalanced(root.left) is True:
        return True
    return False

if __name__ == '__main__':
    root = node(18)
    root.left = node(4)
    root.right = node(20)
    root.right.left = node(13)
    root.right.right = node(70)
    

    print(isbalanced(root))