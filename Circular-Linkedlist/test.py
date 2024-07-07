class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Method to insert at the beginning in constant time
def insert_beg(head, k):
    temp = Node(k)
    if head is None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key, temp.key = temp.key, head.key
        return head

# Method to insert at the end in constant time
def insert_end(head, k):
    temp = Node(k)
    if head is None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key, temp.key = temp.key, head.key
        return temp

# Method to insert at a given position in constant time
def insert_at_position(head, k, pos):
    temp = Node(k)
    if head is None and pos == 1:
        temp.next = temp
        return temp
    
    curr = head
    for _ in range(pos - 2):
        if curr.next == head:
            break
        curr = curr.next
    
    temp.next = curr.next
    curr.next = temp
    return head

# Method to delete from the beginning in constant time
def delete_beg(head):
    if head is None:
        return None
    if head.next == head:
        return None
    head.key = head.next.key
    head.next = head.next.next
    return head

# Method to delete from the end in constant time
def delete_end(head):
    if head is None:
        return None
    if head.next == head:
        return None
    curr = head
    while curr.next.next != head:
        curr = curr.next
    curr.next = head
    return head

# Method to delete from a given position in constant time
def delete_at_position(head, pos):
    if head is None:
        return None
    if pos == 1:
        return delete_beg(head)
    curr = head
    for _ in range(pos - 2):
        if curr.next.next == head:
            break
        curr = curr.next
    curr.next = curr.next.next
    return head

def print_cc(head):
    if head is None:
        return
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next
    print()

if __name__ == '__main__':
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(15)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = head

    head = insert_beg(head, 4)
    head = insert_end(head, 60)
    head = insert_at_position(head, 25, 3)

    print("List after insertions:")
    print_cc(head)

    head = delete_beg(head)
    head = delete_end(head)
    head = delete_at_position(head, 4)

    print("List after deletions:")
    print_cc(head)
