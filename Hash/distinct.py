def dis(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res = res+1
    print("Distict Elements are ",res)
def dis2(l):
    print(len(set(l)))
l=[10,20,30,30,30,30,30,30,30,30,40,40,40,40,40,40]
dis(l)
dis2(l)

