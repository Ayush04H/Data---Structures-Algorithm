'''
A
BB
CCC
DDDD
CCC
BB
A
'''

def func(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(i+64),end="")

        print("")

    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print(chr(i+64),end="")

        print("")


func(4)