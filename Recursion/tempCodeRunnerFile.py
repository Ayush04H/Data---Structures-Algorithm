def oneton(n):
    if n==0:
        return
    oneton(n-1)
    print(n)

if  __name__=='__main__':
    oneton(3)
