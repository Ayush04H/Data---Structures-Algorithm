'''
1
22
333
4444
'''

def func(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")

        print("")

func(3)