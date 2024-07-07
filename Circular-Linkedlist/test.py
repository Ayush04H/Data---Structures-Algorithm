class node:
    def __init__(self,key):
        self.key=key
        self.next=None

# - Author -  Ayush Srivastava

''' Method -1 where we do the insert operation in linear time
'''
def insertbeg_m1(head,k):
    temp=node(k)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while  curr.next != head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return temp

''' Method -2 where we do insert in constant time
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



def printcc(head):
    if head==None:
        return 
    print(head.key,end=" ")
    curr=head.next
    while curr != head:
        print(curr.key,end=" ")
        curr=curr.next

if __name__ == '__main__':
    head=node(5)
    head.next=node(10)
    head.next.next=node(15)
    head.next.next.next = node(30)
    head.next.next.next.next = node(50)
    head.next.next.next.next.next = head
    head=insertbeg_m1(head,4)
    head=insertbeg_m2(head,2)

    printcc(head)