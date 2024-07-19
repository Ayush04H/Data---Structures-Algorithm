class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insert_beg(head, k):
    temp = Node(k)
    temp.next = head
    return temp

def print_list(head):
    curr = head
    while curr:
        print(curr.key, end=" ")
        curr = curr.next
    print()

def partition_list(head, x):
    before,after=Node(0),Node(0)
    before_curr,after_curr=before,after 

    while head:
        if head.key <x:
            before_curr.next,before_curr=head,head
        else:
            after_curr.next,after_curr=head,head
        head=head.next
    after_curr.next=None 
    before_curr.next=after.next 

    return before.next

# Example usage
head = None
keys = [3, 5, 8, 5, 10, 2, 1]
for key in keys:
    head = insert_beg(head, key)

print("Original List:")
print_list(head)

x = 5
head = partition_list(head, x)

print(f"Partitioned List around {x}:")
print_list(head)
