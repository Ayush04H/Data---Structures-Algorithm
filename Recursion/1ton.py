def printNos(n):
    #Your code here
    if n==0:
        return
    printNos(n-1)
    print(n,end=" ")
def printNos2(n):
    #Your code here
    if n==0:
        return
    
    print(n,end=" ")
    printNos(n-1)
if  __name__=='__main__':
    printNos(3)
    print("")
    printNos2(3)
