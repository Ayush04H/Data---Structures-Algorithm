def lomoutopart(a,l,h):
    pivot=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]

    a[i+1],a[h]=a[h],a[i+1]
    return i+1

def quicksort(a,l,h):
    if h>l:
        p=lomoutopart(a,l,h)
        quicksort(a,l,p-1)
        quicksort(a,p+1,h)

arr = [8, 4, 7, 9, 3, 10, 5]
quicksort(arr,0,len(arr)-1)
print(arr)