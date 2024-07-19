class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicatesNoBuffer(head):
    current = head
    
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return head

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Helper function to create a linked list from a list
def insert_beg(head,k):
    temp=Node(k)
    temp.next=head
    return temp


# Example usage:
# LinkedList: 1 -> 2 -> 3 -> 2 -> 1
head=None
head=insert_beg(head,2)
head=insert_beg(head,5)
head=insert_beg(head,5)
head=insert_beg(head,5)
head=insert_beg(head,10)
head=insert_beg(head,10)
head=insert_beg(head,10)
head=insert_beg(head,10)
head=insert_beg(head,30)
head=insert_beg(head,30)
head=insert_beg(head,30)
head=insert_beg(head,2)
head=insert_beg(head,2)
head=insert_beg(head,2)
head=insert_beg(head,2)
removeDuplicatesNoBuffer(head)
printLinkedList(head)  # Output: 1 2 3
