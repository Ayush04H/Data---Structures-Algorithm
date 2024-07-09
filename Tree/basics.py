class node:
      def __init__(self,k):
            self.left=None
            self.right=None
            self.k=k


root=node(30)
root.left=node(40)
root.left=node(70)
root.left.right=node(60)
root.right=node(50)
root.right.left=node(60)
root.right.right=node(80)