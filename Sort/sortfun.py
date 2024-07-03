#Sort Function
l1=[10,4,5,2,3,22,21]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

# Normal case using key 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def myclasss(p):
    return p.x

l=[Point(1,15),Point(10,5),Point(3,8)]
l.sort(key=myclasss)

print("For Normal Case using key")
for i in l:
    print(i.x,i.y)

# without key less than concept
class Point2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        return self.x<other.x

l=[Point2(1,15),Point2(10,5),Point2(3,8)]
l.sort()

print("without key less than concept")
for i in l:
    print(i.x,i.y)

class Point4:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        if self.x == other.x:
            return self.y < other.y
        else:
            self.x < other.x

l=[Point4(1,15),Point4(10,5),Point4(5,8)]
l.sort()

print("without key less equal to concept")
for i in l:
    print(i.x,i.y)

#sorted function
l=[10,-15,-2,1]
ls=sorted(l,key=abs,reverse=True)
print(ls)

#using sorted
class Point3:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        if self.x == other.x:
            return self.y < other.y
        else:
            self.x < other.x

l=[Point3(1,15),Point3(10,5),Point3(5,8)]
l1=sorted(l)
print("without key less equal to concept sorted")
for i in l1:
    print(i.x,i.y)

