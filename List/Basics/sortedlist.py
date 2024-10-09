def issorted(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True

def issorted2(l):
    sl=sorted(l)
    if sl==l:
        return True
    else:
        return False

if __name__=='__main__':
    l=[1,2,3,5,21]
    print(issorted(l))
    print(issorted2(l))