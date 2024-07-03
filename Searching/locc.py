def lastocc(l,x):
    for i in reversed(range(len(l))):
        if l[i]==x:
            return i
    return -1
def lastocc2(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]>x:
            high=mid-1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
l=[10,10,20,20,20,20]
print(lastocc2(l,20))
