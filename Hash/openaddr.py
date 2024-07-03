class MyHash:
    def __init__(self,c):
        self.cap=c
        self.table=[-1]*c
        self.size=0
    def hash(self,x):
        return x%self.cap
    def search(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i]==x:
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False
    def insert(self,x):
        if self.size==self.cap:
            return False
        if self.search(x)==True:
            return False
        i=self.hash(x)
        t=self.table
        while t[i] not in (-1,-2):
            i=(i+1)%self.cap
        t[i]=x
        self.size+=1
        return True
    def prt(self):
        print(self.table)
    def remove(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i]==x:
                t[i]=-2
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False
            

if __name__=='__main__':
    h=MyHash(10)
    h.prt()
    h.insert(12)
    h.insert(18)
    h.insert(13)
    h.insert(2)
    h.insert(3)
    h.insert(23)
    h.insert(5)
    h.insert(15)
    h.prt()