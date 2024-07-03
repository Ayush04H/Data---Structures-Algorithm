def lastocc(l,x):
    for i in reversed(range(len(l))):
        if l[i]==x:
            return i
    return -1
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
def countocc(l,x):
    return lastocc(l,x)-bsearchitr(l,x)+1