def pallindrome(a,i,j):
    while i < j:
        if a[i] != a[j]:
            return False
        i+=1
        j-=1 
    return True

def mcm(a,i,j):
    n=len(a)
    if i>=j or pallindrome(a,i,j):
        return 0
    t = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    if t[i][j] != -1:
        return t[i][j]

    min_cost = float('inf')

    for k in range(i,j):
        cost = (mcm(a,i,k) +
                mcm(a,k+1,j) +
                1)

        if cost < min_cost:
            min_cost=cost

    t[i][j] = min_cost
    return t[i][j] 

def main():
    s = "nitin"  # Example string
    n = len(s)
    
    # Call the function and find the minimum cuts needed
    min_cuts = mcm(s, 0, n - 1)
    print(f"Minimum number of cuts for palindrome partitioning is {min_cuts}")

# Call the main function
main()

  
            