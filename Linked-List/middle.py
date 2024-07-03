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


# 1 st way to solve -- Naive Approach
def printmid(head):
    if head==None:
        return 
    c=0
    curr=head
    while curr!=None:
        c+=1
        curr=curr.next
    curr=head
    for i in range(c//2):
        curr=curr.next
    print(curr.key)

#2 nd way to solve -- Efficient way by using two pointers fast and slow 
def printmid_eff(head):
    if head==None:
        return
    slow=head
    fast=head
    while fast != None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    print(slow.key)



#Main part
head=None
head=insertbegin(head,50)
head=insertbegin(head,40)
head=insertbegin(head,30)
head=insertbegin(head,10)

printlist(head)
print("Way 1")
printmid(head)

print("Way 2")
printmid_eff(head)