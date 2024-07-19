''' Q 2.1 Remove Dups : Write code to remove duplicates from an unsorted linked list
          Follow Up
          How you you solve this problem without a temporary buffer
'''

class node:
    def __init__(self,key):
        self.key=key
        self.next=next

def insert_beg(head,k):
    temp=node(k)
    temp.next=head
    return temp


def printlist(head): 
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next

''' Using temporary buffer  .
'''
def removedup_m1(head):  # - - - - - > > > Time Complexity :O(n) , Space Complexity :O(n) < < < - - - - - #
    if head==None:
        return head
    curr = head
    s=set()
    s.add(curr.key)
    while curr.next != None:
        if curr.next.key in s:
            curr.next=curr.next.next
        else:
            s.add(curr.next.key)
            curr=curr.next 
             
    return head


''' Not Using temporary buffer .
'''
def removeDuplicatesNoBuffer(head):
    current = head
    
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.key == current.key:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return head

if __name__ == '__main__':
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
    print("Before removing duplicates\n")
    printlist(head)
    removedup_m1(head)
    print("After removing duplicates\n")
    printlist(head)



    
    