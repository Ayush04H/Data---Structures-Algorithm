class node:
    def __init__(self, k):
        self.next = None
        self.prev = None
        self.key = k

def insertbeg(head, k):
    temp = node(k)
    if head is not None:
        head.prev = temp
    temp.next = head
    return temp

def insertend(head, k):
    temp = node(k)
    if head is None:
        return temp
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head

def insert_at_position(head, k, position):
    temp = node(k)
    # Inserting at the head if position is 1
    if position == 1:
        if head is not None:
            head.prev = temp
        temp.next = head
        return temp

    curr = head
    curr_position = 1
    while curr is not None and curr_position < position:
        prev_node = curr
        curr = curr.next
        curr_position += 1

    # If we reached the end of the list, insert at the end
    if curr is None:
        prev_node.next = temp
        temp.prev = prev_node
    else:
        # Inserting in the middle
        prev_node.next = temp
        temp.prev = prev_node
        temp.next = curr
        curr.prev = temp

    return head

def printdll(head):
    if head is None:
        return
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

def delete_beg(head):
    if head==None:
        return None 
    if head.next==None:
        return None 
    else:
        head=head.next 
        head.prev=None
        return head
    
def delete_last(head):
    if head==None:
        return None
    if head.next == None:
        return None

    curr=head
    while curr.next.next != None:
        curr=curr.next 
    curr.next=None 
    return head

if __name__ == '__main__':
    head = None
    head = insertbeg(head, 5)
    head = insertbeg(head, 4)
    head = insertbeg(head, 2)
    head = insert_at_position(head, 6, 2)
    head=insertend(head,9)
    head=insertend(head,10)
    head=insertend(head,12)
    head=insertend(head,13)
    head=insertend(head,16)
    
    print("Original list:")
    printdll(head)

    # List after deletion 
    print("List after deletion ")
    head=delete_beg(head)
    head=delete_last(head)
    
    printdll(head)
