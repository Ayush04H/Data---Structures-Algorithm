def hoare(a,l,h):
    pivot=a[l]
    i=l-1
    j=h+1
    while True:
        i+=1
        while a[i]<pivot:
            i+=1
        j-=1
        while a[j]>pivot:
            j-=1
        if i>=j:
            return j
        a[i],a[j]=a[j],a[i]

def quicksort(a,l,h):
    if h>l:
        p=hoare(a,l,h)
        quicksort(a,l,p)
        quicksort(a,p+1,h)

arr = [8, 4, 7, 9, 3, 10, 5]
quicksort(arr,0,len(arr)-1)
print(arr)