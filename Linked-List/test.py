class node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printlist(head):
    curr=head
    while curr!= None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")
def insertbegin(head,k):
    temp=node(k)
    temp.next=head
    return temp


def issorted(head):
    if head==None:
        return 1
    curr=head
    while curr!=None:
        if curr.key > curr.next.key:
            return 0
        curr=curr.next
    return 1






#Main part
head=None
head=insertbegin(head,50)
head=insertbegin(head,40)
head=insertbegin(head,30)
head=insertbegin(head,10)
issorted(head)

printlist(head)
