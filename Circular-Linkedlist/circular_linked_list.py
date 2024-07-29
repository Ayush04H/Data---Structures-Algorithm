class node:
    def __init__(self,key):
        self.key=key
        self.next=None

# - Author -  Ayush Srivastava

''' Method -1 where we do the insert operation in linear time
'''


''' Method -2 where we do insert in constant time  - O(1)
'''

def insertbeg_m2(head,k):
    temp=node(k)
    if head==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        head.key,temp.key=temp.key,head.key
        return head

def insert_end_m2(head,k):
    temp=node(k)
    if head== None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        temp.key,head.key=head.key,temp.key
        return temp


def insert_pos(head, k, pos):
    temp = node(k)
    if head is None or pos == 1:
        temp.next = temp
        return temp
    
    curr = head
    for i in range(pos - 2):
        if curr.next == head:
            break
        curr = curr.next
    
    temp.next = curr.next
    curr.next = temp
    return head


def delete_head(head):
    if head==None:
        return None
    elif head.next == head:
        return None
    else:
        head.key=head.next.key
        head.next=head.next.next 
        return head

def delete_pos(head,pos):
    if head==None:
        return None
    elif pos==1:
        delete_head(head)
    curr=head
    for i in range(pos-2):
        curr=curr.next
    curr.next=curr.next.next
    return head

def length_of_list(head):
    c=1
    if head==None:
        return 
    curr=head.next
    while curr != head:
        curr=curr.next
        c+=1
    return c

def delete_last(head):
    pos=length_of_list(head)
    return delete_pos(head,pos)

def printcc(head):
    if head==None:
        return 
    print(head.key,end=" ")
    curr=head.next
    while curr != head:
        print(curr.key,end=" ")
        curr=curr.next

if __name__ == '__main__':

    # Inserting Data
    head=node(5)
    head.next=node(10)
    head.next.next=node(15)
    head.next.next.next = node(30)
    head.next.next.next.next = node(50)
    head.next.next.next.next.next = head
    head=insertbeg_m2(head,4)
    head=insertbeg_m2(head,2)
    head=insert_end_m2(head,99)
    head=insert_pos(head,3,2)
    head=insert_pos(head,7,5)

    printcc(head)
    print("\n")

    # Deleting Data
    head=delete_head(head)
    head=delete_pos(head,2)
    head=delete_last(head)

    printcc(head)