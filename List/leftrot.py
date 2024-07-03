def rot(l):
    l.append(l.pop(0))
    print(l)
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8]
    rot(l)