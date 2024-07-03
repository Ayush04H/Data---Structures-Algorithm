def merge(a,l,m,h):
    left=a[l:m+1]
    right=a[m+1:h+1]
    k=l
    i=j=res=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k]=right[j]
            j+=1
            k+=1
            res+=len(left)-i
    while i<len(left):
        a[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        a[k]=right[j]
        j+=1
        k+=1
    return res
def mergesort(a,l,r):
    res=0
    if r>l:
        m=(r+l)//2
        res+=mergesort(a,l,m)
        res+=mergesort(a,m+1,r)
        res+=merge(a,l,m,r)
    return res
l = [1, 20, 6, 4, 5]
print(mergesort(l,0,len(l)-1))


