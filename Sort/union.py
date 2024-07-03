# union of two sorted arrays
# a=[1,4,9]
# b=[2,3,4,4,4,4,5,6,7,8,9,10,99]

def printu(a,b):
    c=a+b
    c.sort()
    for i in range(0,len(c)):
        if (i==0 or c[i]!=c[i-1]):
            print(c[i],end=" ")

def printu2(a,b):
    i=j=0
    while(i<len(a) and j<len(b)):
        if (i>0 and a[i]==a[i-1]):
            i+=1
        elif (j>0 and b[j]==b[j-1]):
            j+=1
        elif(a[i]<b[j]):
            print(a[i],end=" ")
            i+=1
        elif(a[i]>b[j]):
            print(b[j],end=" ")
            j+=1
        else:
            print(a[i],end=" ")
            i+=1
            j+=1
    while(i<len(a)):
        if (i>0 and a[i]!=a[i-1]):
            print(a[i],end=" ")
            i+=1
    while(j<len(b)):
        if (j>0 and b[j]!=b[j-1]):
            print(b[j],end=" ")
            j+=1



a=[1,4,9,9,9,9,9,9,9,9,9,9,9,9,99]
b=[2,3,4,4,4,4,5,6,7,8,9,10,99]
printu2(a,b)