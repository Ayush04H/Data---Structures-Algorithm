def leftrot(l):
    l.append(l.pop(0))
    print(l)


def rightrot(l):
    l.insert(0,l.pop())
    print(l)


if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8]
    leftrot(l)

    l2 =[1,2,3,4]
    rightrot(l2)