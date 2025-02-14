'''
   A
  AB
 ABC
ABCD
'''

def func(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=n-i:
                print(" ",end="")

            else:
                print(chr(j-(n-i)+64),end="")

        print()


func(4)