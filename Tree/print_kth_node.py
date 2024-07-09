class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def print_nth_node(root,k):
    if root==None:
        return
    if k==0:
        print(root.key,end=" ")
    else:
        print_nth_node(root.left,k-1)
        print_nth_node(root.right,k-1)
        

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

    print_nth_node(root,0)