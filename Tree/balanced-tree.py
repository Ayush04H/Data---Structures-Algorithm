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
def is_balanced_2(root):
    if root==None:
        return 0
    lh=is_balanced_2(root.left)
    if lh ==-1:
        return -1
    rh=is_balanced_2(root.right)
    if rh == -1:
        return -1
    if abs(lh-rh) >1:
        return -1
    return max(lh,rh) + 1

def is_balanced_main(root):
    if is_balanced_2(root) ==-1:
        return False
    return True

if __name__ == '__main__':
    root = node(18)
    root.left = node(4)
    root.right = node(20)
    root.right.left = node(13)
    root.right.right = node(70)
    root.right.right.left=node(30)
    

    print(isbalanced(root))
    print(is_balanced_main(root))