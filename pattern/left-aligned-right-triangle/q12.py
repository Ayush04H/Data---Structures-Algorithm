'''
A
AB
ABC
ABCD
ABCDE
'''

def func(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(j+64),end="")

        print("")

func(5)