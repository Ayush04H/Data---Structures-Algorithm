''' Q2 2.3 Delete Middle Node
'''

class node:
    def __init__(self,key):
        self.key=key
        self.next=next 

def insert_beg(head,k):
    temp=node(k)
    temp.next=head
    return temp

def count_node(head):
    if head==None:
        return 
    c=0
    curr=head
    while curr != None:
        c+=1
        curr=curr.next
    return c

def delete_beg(head):
    if head==None:
        return 
    n=head.next
    head.next=None 
    return n

def delete_pos(head,pos):
    if head==None:
        return 
    if pos==1:
        delete_beg(head)
    temp=head 
    for i in range(pos-2):
        temp=temp.next 
    temp.next=temp.next.next 
    return head

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
    c=count_node(head)
    head=delete_pos(head,c//2 +1)
    printhead(head)