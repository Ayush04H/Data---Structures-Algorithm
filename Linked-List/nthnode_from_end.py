class node:
    def __init__(self,key):
        self.key=key
        self.next=None
def insertbeg(head,k):
    temp=node(k)
    temp.next=head
    return temp

def printlist(head):
    if head==None:
        print("No List")
    curr=head
    while curr != None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")

def insertend(head,k):
    if head==None:
        return node(k)
    curr=head
    while curr.next!= None:
        curr=curr.next
    curr.next=node(k)
    return head

# Method 1 
'''In this method we proceed by calculating the size of the Linked List
    time complexity O(m)
    space complexity O(1)

'''
def nthnode_end_m1(head,pos):
    n=0
    if head==None:
        return
    curr=head
    while curr!= None:
        curr=curr.next
        n+=1
    print("The length of ll is ",n)
    curr=head
    for i in range(n-pos):
        curr=curr.next
    if pos>n:
        print("Number of nodes less than pos\n")
    else:
        print(curr.key)

''' Method 2
    In this method we have two pointer concept 
    1- which is the mentioned postioned ahead of the 2nd

    time complexity O(m)
    space complexity O(1)
'''

def nthnode_end_m2(head,pos):
    if head==None:
        return 
    first=second=head
    for i in range(pos):
        if first==None:
            return
        first=first.next
    while first != None:
        second=second.next
        first=first.next
    print(second.key)


if __name__ =='__main__':
    head=None
    head=insertbeg(head,5)
    head=insertbeg(head,3)
    head=insertbeg(head,1)
    head = insertend(head,7)
    head = insertend(head,9)
    head = insertend(head,11)
    printlist(head)

    nthnode_end_m1(head,2)
    nthnode_end_m2(head,2)