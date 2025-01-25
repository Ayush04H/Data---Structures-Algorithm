class Node:
    def __init__(self,k):
        self.key = k;
        self.next = None;

def insert_beg(head,k):
    temp = Node(k);
    temp.next = head;
    return temp;

def insert_end(head,k):
    if head == None:
        return Node(k);
    curr = head 
    while curr.next != None:
        curr = curr.next; 
    curr.next = Node(k);
    return head;


def insert_pos(head,pos,k):
    temp = Node(k)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
        
    temp.next = curr.next 
    curr.next = temp 
    return head

def delete_beg(head):
    if head == None:
        return None
    new = head.next 
    head.next = None
    return new

def delete_end(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next 
    curr.next = None 
    return head

def delete_pos(head,pos):
    if pos == 1:
        new = head.next 
        head.next = None
        return new 
    
    temp = head 
    for i in range(pos-2):
        temp = temp.next 
    temp.next = temp.next.next 
    return head

def printhead(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")

if __name__ == "__main__":
    head = None
    head = insert_beg(head,5)
    head = insert_beg(head,10)
    head = insert_beg(head,15)
    head = insert_end(head,20)
    head = insert_end(head,30)
    head = insert_pos(head,5,25)
    print("Before Delete")
    printhead(head)
    print("After Delete")
#    head = delete_beg(head)
#    head = delete_end(head)
    head = delete_pos(head,2)
    printhead(head)