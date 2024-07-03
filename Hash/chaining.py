class MyHash:
    def __init__(self,b):
        self.bucket=b
        self.table=[[] for x in range(b)]
    def insert(self,x):
        i=x%self.bucket
        self.table[i].append(x)
    def remove(self,x):
        i=x%self.bucket
        if x in self.table[i]:
            self.table[i].remove(x)
    def search(self,x):
        i=x%self.bucket
        return x in self.table[i]
    def prt(self):
        print(self.table)
    

if __name__=='__main__':
    h=MyHash(7)
    h.insert(3)
    h.insert(2)
    h.insert(4)
    h.insert(5)
    h.insert(1)
    h.insert(8)
    print(h.search(4))
    print(h.search(5))
    print(h.search(6))
    h.remove(4)
    print(h.search(4))
    h.prt()