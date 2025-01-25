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

def insertbegin(head,k):
    temp=node(k)
    temp.next=head
    return temp

def insertend(head,k):
    if head==None:
        return node(k)      
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=node(k)
    return head

def insertpos(head,data,pos):
    temp=node(data)
    if pos==1:
        insertbegin(head,data)
    curr=head
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head

def delbeg(head):
    if head==None:
        return None
    new=head.next
    head.next=None
    return new

def dellast(head):
    if head==None:
        return None
    if head.next==None:
        return None
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head

def delpos(head,pos):
    if pos==1:
        new=head.next
        head.next=None
        return new
    temp=head
    for i in range(pos-2):
        temp=temp.next
    temp.next=temp.next.next
    return head

def searchitem(head,item):
    curr=head
    c=1
    while curr!=None:
        if curr.key==item:
            print(f"{item} Key is found at node {c}")
            break
        c+=1
        curr=curr.next
head=None
temp1=node(10)
temp2=node(20)
temp3=node(30)
temp4=node(40)
temp1.next=temp2
temp2.next=temp3
temp3.next=temp4
head=temp1

head=insertbegin(head,5)
head=insertbegin(head,15)
head=insertend(head,100)
head=insertpos(head,25,2)
printhead(head)
#head=delbeg(head)
#printhead(head)
#head=dellast(head)
#printhead(head)
head=delpos(head,3)
printhead(head)



