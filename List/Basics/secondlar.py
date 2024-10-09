def getmax(l):
    max=l[0]
    for x in l:
        if x>max:
            max=x
    return max
def secondmax(l):
    lar=getmax(l)
    slar=None
    if len(l)<=1:
        return None
    for x in l:                           #double traversal
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar
def secondmax2(l):
    lar=getmax(l)
    slar=0
    if len(l)<=1:                        #Single Traversal
        return None
    for x in l:
        if x>slar and x<lar:
            slar=x
    if slar!=0:
        return slar
    else:
        return None
if __name__=='__main__':
    l=[20,20,10,60]
    print(getmax(l))
    print(secondmax(l))
    print(secondmax2(l))
