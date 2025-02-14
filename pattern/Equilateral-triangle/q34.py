'''
ABCDEDCBA
 ABCDCBA 
  ABCBA  
   ABA   
    A    
'''

def func(n):
    # Lower triangle
    for i in range(n,0,-1):
        num = 1
        for j in range(1, 2 * n):
            if j >= n - (i - 1) and j <= n + (i - 1):
                print(chr(num+64), end="")
                if j < n:
                    num += 1
                else:
                    num -= 1
            else:
                print(" ", end="")
        print()

func(5)
