class node:
    def __init__(self,k):
        self.key=k
        self.next=None


def printhead(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")

def sortedins(head,x):
    temp=node(x)
    if head==None:
        return temp
    elif x < head.key:
        temp.next=head
        return temp
    else:
        curr=head
        while curr.next!=None and curr.next.key <x:
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
        return head
    
def insertbegin(head,k):
    temp=node(k)
    temp.next=head
    return temp
    



head=None
head=insertbegin(head,50)
head=insertbegin(head,40)
head=insertbegin(head,30)
head=insertbegin(head,10)
head=sortedins(head,20)
#print(issorted(head))
printhead(head)