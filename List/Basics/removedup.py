def removedup(l,n):
    res=1
    temp=[0]*n
    temp[0]=l[0]
    for i in range(1,n):
        if temp[res-1]!=l[i]:
            temp[res]=l[i]
            res+=1
    for i in range(0,res):
        l[i]=temp[i]
    print(f"Size after removal of duplicates {res}")
    print(l[:res])
def removedup2(l,n):
    res=1
    for i in range(1,n):
        if l[res-1]!=l[i]:
            l[res]=l[i]
            res+=1
    print(res)
    print(l[:res])
if __name__=='__main__':
    l=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,0,0,0,0,0,0,0,00,0,0,0,0,6,6,6,6,6,6,6,66,6,6,00,0,0,4,4,4,4]
    n=len(l)
    removedup2(l,n)