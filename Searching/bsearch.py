def bsearch(l,x):
    low=0
    high=len(l)-1
    
    while low<=high :
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
def bsearch2(l,x,low,high):
    mid=(low+high)//2
    if low>high:
        return -1
    if l[mid]==x:
        return mid
    elif l[mid]<x:
        low=mid+1
        return bsearch2(l,x,low,high)
    else:
        high=mid-1
        return bsearch2(l,x,low,high)
if __name__=='__main__':
    l=[10,20,40,40,12,124,134,162]
    l.sort()
    print(l)
    x=0
    print(bsearch2(l,x,0,len(l)))