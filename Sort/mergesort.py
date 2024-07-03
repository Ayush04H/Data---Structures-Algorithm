def merge(a,l,m,h):
    left=a[l:m+1]
    right=a[m+1:h+1]
    k=l
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        a[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        a[k]=right[j]
        j+=1
        k+=1
def mergesort(a,l,r):
    if r>l:
        m=(r+l)//2
        mergesort(a,l,m)
        mergesort(a,m+1,r)
        merge(a,l,m,r)

l=[10,8,20,5,110,0,63,87,12,11]
mergesort(l,0,len(l)-1)
print(l)

