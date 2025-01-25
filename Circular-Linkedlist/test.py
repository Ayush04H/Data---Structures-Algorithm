class Node:
    def __init__(self,k):
        self.key = k
        self.next = None 


def insert_beg(head,k):
    temp = Node(k)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next 
        head.next = temp 
        head.key,temp.key = temp.key ,head.key 
        return head

def insert_end(head,k):
    temp = Node(k)
    if head == None:
        temp.next = temp 
        return temp 
    else:
        temp.next = head.next 
        head.next = temp 
        temp.key,head.key = head.key,temp.key
        return temp
    
def insert_pos(head,k,pos):
    temp = Node(k)
    if head == None or pos == 1:
        temp.next = temp
        return temp 
    curr = head 
    for i in range(pos-2):
        if curr.next == None:
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

def delete_end(head):
    if head == None:
        return None 
    elif head.next == head:
        return None 
    curr = head 
    while curr.next.next != head:
        curr = curr.next 
    curr.next = head
    return head

def delete_pos(head,pos):
    if head == None:
        return None 
    if head.next == head:
        return None
    if pos == 1:
        head.key = head.next.key
        head.next = head.next.next 
        return head 
    else:
        curr = head 
        for i in range(pos-2):
            curr = curr.next 
        curr.next = curr.next.next 
        return head 

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
    head = None
    head = insert_beg(head,10)
    head = insert_beg(head,40)
    head = insert_end(head,50)
    head = insert_end(head,60)
    head = insert_pos(head,20,3)

    print("Before Inserting Data")
    printcc(head)

    print("\nAfter Inserting Data")
   # head = delete_head(head)
   # head = delete_end(head)
    head = delete_pos(head,3)
    printcc(head)