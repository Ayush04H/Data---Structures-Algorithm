class node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printcc(head):
    if head==None:
        return 
    print(head.key,end=" ")
    curr=head.next
    while curr != head:
        print(curr.key,end=" ")
        curr=curr.next



head=node(5)
head.next=node(10)
head.next.next=node(15)
head.next.next.next = node(30)
head.next.next.next.next = node(50)
head.next.next.next.next.next = head

printcc(head)