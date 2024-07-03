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
    return lastocc2(l,x)-bsearchitr(l,x)+1

l=[10,10,20,20,20,20]
print(countocc(l,20))