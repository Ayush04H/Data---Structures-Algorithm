class node:
    def __init__(self,key):
        self.key=key
        self.next=None



def insertbeg(head,k):
    temp=node(k)
    temp.next=head
    return temp

def insertend(head,k):
    if head==None:
        return node(k)
    curr=head
    while curr.next !=None:
        curr=curr.next
    curr.next=node(k)
    return head

def insertpos(head,k,pos):
    temp=node(k)
    if pos==1:
        insertbeg(head,k)
    curr=head
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head


def printlist(head):
    if head==None:
        return 
    curr=head
    while curr != None:
        print(curr.key,end=" ")
        curr=curr.next

''' First approach using a stack  --> Naive Approach
'''

def reversel_m1(head):
    stack=[]
    curr=head
    while curr != None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr != None:
        curr.key=stack.pop()
        curr=curr.next
    return head


''' Second approach --> Instead of reversing the list we reverse the links to the Linked List
    My maintaining 3 Variables
'''

def reversel_m2(head):
    curr = head
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


if __name__=='__main__':
    head=None
    head=insertbeg(head,10)
    head=insertbeg(head,2)
    head=insertend(head,80)
    head=insertpos(head,4,2)
    print("Printing the list before reversal\n")
    printlist(head)
    head=reversel_m1(head)
    print("Printing the list after reversal\n")
    printlist(head)