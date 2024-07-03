def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

l=[1,4,7,9,7,6,5,0,100]
bubblesort(l)
print(l) 

#opptimized bubble sort
def bubblesort2(l):
    n=len(l)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if swapped == False:
            return
l=[10,8,20,5,110,0,63,87,12,11]
bubblesort2(l)
print(l) 