def initialize_matrix(rows: int, cols: int, value: int) -> list:
    return [[value for _ in range(cols)] for _ in range(rows)]

def knapsack(W : int , val :list[int] , weight :list[int] ,n :int) -> int :
    if W == 0 or n == 0:
        return 0 
    t = initialize_matrix(n+1 ,W +1 ,-1)

    if t[n][W] != -1:
        return t[n][W]

    
    if weight[n-1] <= W :
        t[n][W] = max(val[n-1] + knapsack(W-weight[n-1] , val , weight , n-1) ,  knapsack(W, val , weight ,n-1))
        return t[n][W]
    elif weight[n-1] > W:
        t[n][W] = knapsack(W, val , weight ,n-1)
        return t[n][W]
    

# Time :O(2 ^ n) 
# Space :O(n)
def main():
    # Example values for the knapsack problem
    W = 7  # Maximum weight capacity of the knapsack
    val = [1, 4, 5 , 7]  # Values of the items
    weight = [1 , 3 ,4 ,5]  # Weights of the items
    n = len(val)  # Number of items


    # Call the knapsack function
    result = knapsack(W, val, weight, n)
    
    # Print the result
    print("Maximum value that can be obtained:", result)

if __name__ == "__main__":
    main()