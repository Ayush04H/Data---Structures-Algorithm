class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None


def insert_recc(root,k):
    if root==None:
        return Node(k)
    elif root.key == k:
        return root 
    elif root.key > k:
        root.left=insert_recc(root.left,k)
    else:
        root.right=insert_recc(root.right,k)
    return root 

def insert_itr(root,k):
    temp = Node(k)
    parent=None 
    curr=root 
    while curr:
        parent = curr 
        if curr.key == k:
            return root 
        elif curr.key > k:
            curr=curr.left 
        else:
            curr = curr.right 
    
    if parent == None:
        return temp 
    elif parent.key > k:
        parent.left = temp 
    else:
        parent.right = temp 
    
    return root


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


# For deleting 
def getsucc(curr):
    while curr.left:
        curr=curr.left 
    return curr 

def delete_node(root,k):
    if root == None:
        return
    if root.key > k:
        root.left = delete_node(root.left,k)
    elif root.key <k:
        root.right =delete_node(root.right,k)
    else:
        if root.left == None:
            return root.right 
        elif root.right == None:
             return root.left 
        else:
            succ=getsucc(root.right)
            root.key=succ 
            root.right=delete_node(root.right,succ)

    return root


def getFloor(root,x):
    res = None

    while root != None:
        
        if root.key == x:
            return root.key
        elif root.key>x:
            root = root.left
        else:
            res = root.key
            root = root.right
    
    return res


def getCeil(root,x):
    res = None

    while root != None:
        
        if root.key == x:
            return root.key
        elif root.key>x:
            res = root.key
            root = root.left
        else:
            root = root.right
    
    return res
    
    


if __name__ == '__main__':
    root=Node(10)
    root=insert_itr(root,5)
    root=insert_itr(root,15)
    root=insert_itr(root,12)
    root=insert_itr(root,30)
    print("Before deleteion")
    inorder_traversal(root)

    print("\n")

    print(getFloor(root,100))
    print(getCeil(root,13))