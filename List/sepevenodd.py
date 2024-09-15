def evenodd(l):
    l1=[]
    l2=[]
    for i in range(0,len(l)):
        if l[i]%2==0:
            l1.append(l[i])
        else:
            l2.append(l[i])

    return l1,l2


def evenoddtwop(l):
    i=0 
    j=len(l)-1

    while i<j:
        if l[i] %2 !=0:
            i+=1

        elif l[j] %2 == 0:
            j-=1

        else:
            l[i],l[j] = l[j],l[i]
            i+=1
            j-=1

    return l
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8,9,10,11,2,25,41,89,85,68,58,56,70]
    even,odd=evenodd(l)
    print(even)
    print(odd)
    print(evenoddtwop(l))
