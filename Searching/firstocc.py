def lsearch(l,x):
    for i in range(0,len(l)):
        if l[i]==x:
            return i
    return -1
def bsearchrec(arr,l,h,x):
    if l>h:
        return -1
    mid=(l+h)//2
    if arr[mid]<x:
        l=mid+1
        return bsearchrec(arr,l,h,x)
    elif arr[mid]>x:
        h=mid-1
        return bsearchrec(arr,l,h,x)
    else:
        if mid==0 or arr[mid-1]!=arr[mid]:
            return mid
        else:
            return bsearchrec(arr,l,mid-1,x)
def bsearchitr(arr,x):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]<x:
            l=mid+1
        elif arr[mid]>x:
            h=mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                h=mid-1
    return -1
l=[0,1,3,4,4,4,4,4,4,4,4,4,4,4,4]
print(bsearchrec(l,0,len(l)-1,4))