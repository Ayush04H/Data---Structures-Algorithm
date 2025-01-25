# Using a While Lopp 
def pallindrome():
    s = input("Enter a String:\n")
    low = 0

    high = len(s)-1

    while low<high:
        if s[low]!=s[high]:
            print("No")
            break
        low = low+1
        high = high-1
        
    else:
        print("Yes")


# Using Slicing In Python:

def pallindrome2():
    s = input("Enter the STring\n")
    if s == s[::-1]:
        print('Yes')

    else:
        print('No')

str1 = 'aba'
#pallindrome()
pallindrome2()
        