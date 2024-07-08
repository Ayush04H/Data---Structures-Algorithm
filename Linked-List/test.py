class node:
    def __init__(self,key):
        self.key=key
        self.next=None

def insert_beg(head,k):
    temp=node(k)
    temp.next=head
    return temp


def insert_end(head,k):
    if head==None:
        return node(k) 
    curr=head 
    while curr.next != None:
        curr=curr.next
    curr.next=node(k)
    return head 

def insert_pos(head,k,pos):
    if head==None or pos==1:
        return insert_beg(head,k)
    curr=head
    for i in range(pos-2):
        curr=curr.next
    temp=node(k)
    temp.next=curr.next
    curr.next=temp
    return head

def delete_beg(head):
    if head==None:
        return 
    n=head.next
    head.next=None
    return n

def delete_end(head):
    if head==None:
        return
    if head.next==None:
        return
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
def delete_pos(head,pos):
    if pos==1:
        return delete_beg(head)
    temp=head
    for i in range(pos-2):
        temp=temp.next
    temp.next=temp.next.next
    return head

def removedup(head):
    if head==None:
        return
    curr=head
    while curr!= None and curr.next !=None:
        if curr.key==curr.next.key:
            curr.next=curr.next.next 
        else:
            curr=curr.next 
def printhead(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")


if __name__ == '__main__':
    head=None
    head=insert_beg(head,10)
    head=insert_end(head,100)
    head=insert_end(head,99)
    head=insert_pos(head,20,2)
    head=insert_pos(head,90,3)
    head=insert_pos(head,9,1)
    head=insert_pos(head,20,1)
    head=insert_pos(head,9,1)
    head=insert_pos(head,99,5)
    head=insert_pos(head,99,5)

    print("Printing List after insertion")
    printhead(head)
    removedup(head)
    print("Duplicates removed  from list\n")
    printhead(head)
