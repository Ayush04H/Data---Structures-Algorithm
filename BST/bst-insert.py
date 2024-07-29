class Node:
    def __init__(self,key):
        self.key = key 
        self.right = None 
        self.left = None

def insert_recc(root,k):
    if root==None:
        return Node(k)
    elif root.key == k:
        return root 
    elif root.key > k:
        root.left = insert_recc(root.left,k)
    else:
        root.right = insert_recc(root.right,k)
    return root

def insert_itr(root,k):
    temp=Node(k)
    parent=None 
    curr=root 
    while curr:
        parent=curr 
        if curr.key == k:
            return root 
        elif curr.key > k:
            curr=curr.left
        else:
            curr=curr.right 

    if parent.key == k:
        return temp
    elif parent.key > k:
        parent.left=temp
    else:
        parent.right=temp 
    return root
    
    

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


if __name__ == '__main__':
    root=Node(55)
    root=insert_recc(root,50)
    root=insert_recc(root,100)
    root=insert_recc(root,150)
    root=insert_recc(root,20)
    root=insert_recc(root,10)
    root=insert_recc(root,5)
    root=insert_recc(root,17)
    root=insert_recc(root,117)
    root=insert_recc(root,60)
    root=insert_recc(root,70)
    root=insert_recc(root,80)
    root=insert_itr(root,180)
    root=insert_itr(root,11)
    root=insert_itr(root,12)

    inorder_traversal(root) 