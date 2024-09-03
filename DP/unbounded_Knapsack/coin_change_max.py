def count_subset( arr:list[int] , Sum:int):
    n=len(arr)
    t = [[0 for _ in range(Sum + 1)]for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1

    for i in range(1,n+1):
        for s in range(1,Sum + 1):
            if arr[i-1] <= s:
                t[i][s] = t[i][s - arr[i-1]] + t[i -1][s]
            else:
                t[i][s] = t[i -1][s]

    return t[n][Sum]


def main():
    # Example values for the Subset Sum problem
    arr = [1 , 2 , 3]  # Set of numbers
    sum_val = 5  # Desired sum
    
    # Call the subset_sum function
    result = count_subset(arr, sum_val)
    
    # Print the result
    print("Maaximum number of Subset possible are ", result)

if __name__ == "__main__":
    main()
