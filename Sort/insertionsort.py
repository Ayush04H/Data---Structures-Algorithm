def insertionSort(l):

    for i in range(1,len(l)):
        x = l[i]
        j = i-1

        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1

        l[j+1] = x
        
l=[10,8,20,5,110,0,63,87,12,11]

insertionSort(l)
print(l)
