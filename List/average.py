def avglst(l):
    s=0
    for x in l:
        s+=x
    n=len(l)
    return s/n
def avglst2(l):
    return sum(l)/len(l)
if __name__ =='__main__':
    l=[10,20,30,40,50]
    print(avglst(l))
    print(avglst2(l))