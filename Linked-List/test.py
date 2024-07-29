class node:
    def __init__(self,k):
        self.key=k
        self.next=None 

def insert_beg(head,k):
    temp=node(k) 
    temp.next =head 
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
    temp=node(k)
    if head==None or pos==1:
        temp.next=head 
        return temp 
    curr=head 
    for i in range(pos-2):
        curr=curr.next 
        if curr == None:
            return 
    
    temp.next=curr 
    curr.next=temp 
    return head

def delete_beg(head):
    if head==None:
        return None 
    new=head.next
    head.next=None 
    return new

def delete_last(head):
    if head==None:
        return None
    if head.next==None:
        return None
    curr=head 
    while curr.next.next != None:
        curr=curr.next
    curr.next=None 
    return head 

def delete_pos(head,pos):
    if  head==None:
        return 
    if pos==1:
        new=head.next 
        head.next=None 
        return new
    curr=head 
    for i in range(pos-2):
        curr=curr.next 
    curr.next=curr.next.next 
    return head

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")


    

if __name__ == "__main__":
    head=None 
    head=insert_beg(head,30)
    head=insert_beg(head,20)
    head=insert_beg(head,10)
    head=insert_end(head,80)
    head=insert_end(head,85)
    head=insert_end(head,90)    
    head=insert_end(head,95)    
    head=insert_end(head,100)    
    print("List After Insertion")
    printlist(head)

    #head=delete_last(head)
    head=delete_pos(head,4)
    print("List After Deletion")
    printlist(head)
