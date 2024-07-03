n=int(input("Enter the Number-"))
res=0
while n>0:
    n//=10
    res+=1

print(f"Digits Present - {res}")