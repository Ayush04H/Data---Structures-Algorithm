'''
1
22
333
4444
333
22
1
'''

def func(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")

        print("")

    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print(i,end="")

        print("")


func(4)