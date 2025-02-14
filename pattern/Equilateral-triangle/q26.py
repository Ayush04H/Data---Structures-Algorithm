'''
    1    
   222   
  33333  
 4444444 
555555555
'''

def func(n):
    for i in range(1,n+1):
        for j in range(1,2*n):
            if j >= n-(i-1) and j <= n+(i-1):
                print(i,end="")
            else:
                print(" ",end="")

        print()


func(5)
