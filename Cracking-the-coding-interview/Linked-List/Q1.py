''' Q1 2.2- Return Kth to Last : Implement an algo to find the kth to last element of a singly linked lis
'''

class node:
    def __init__(self,key):
        self.key= key
        self.next =next

def insert_beg(head,k):
    temp=node(k)
    temp.next=head
    return temp

def kth_node(head,n):
    first=second=head
    if head==None:
        return 
    for i in range(n):
        first=first.next 
    while first != None:
        first=first.next
        second=second.next 
    print( n," element from the last is ",second.key)

def printhead(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")
if __name__== '__main__':
    head=None
    head=insert_beg(head,100)
    head=insert_beg(head,90)
    head=insert_beg(head,80)
    head=insert_beg(head,70)
    head=insert_beg(head,60)
    head=insert_beg(head,50)

    printhead(head)
    kth_node(head,2)
