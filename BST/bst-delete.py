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
    temp=Node(k)
    parent=None 
    curr=root 
    while curr :
        parent=curr 
        if curr.key == k:
            return root 
        elif curr.key >k:
            curr=curr.left 
        else:
            curr=curr.right 
    
    if parent.key == k:
        return temp 
    elif parent.key > k:
        parent.left =temp 
    else:
        parent.right = temp
    return root

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


# For deleting 
def getsucc(curr,key):
    while curr.left:
        curr=curr.left 
    return curr

def delete_node(root,k):
    if root == None:
        return 
    if root.key > k:
        root.left = delete_node(root.left,k)
    elif root.key < k:
        root.right = delete_node(root.right,k)
    else:
        if root.right == None:
            return root.left
        elif root.left == None:
            return root.right 
        else:
            succ=getsucc(root.right,k)
            root.key=succ
            root.right=delete_node(root.right,succ)

    return root


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
    print("Before deleteion")
    inorder_traversal(root)

    print("\n")

    root=delete_node(root,17)
    print("After deleteion")
    inorder_traversal(root) 