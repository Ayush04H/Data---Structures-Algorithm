def pallindrome():
    n=int(input("Enter the Number-"))
    temp=n
    rev=0
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp//=10
    return rev==n

if __name__ =='__main__':
    print(pallindrome())