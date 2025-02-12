'''
4444
333
22
1
'''

def func(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(i,end="")

        print("")


func(5)