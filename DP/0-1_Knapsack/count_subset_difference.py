# Same for target sum 


def count_subset_difference(arr : list[int] , diff : int ) -> int :
    Sum = sum(arr)
    n = len(arr) 


    if (diff + Sum) % 2 != 0 :
        return 0
    
    total_sum = (diff + Sum) // 2

    t = [[0 for _ in range(total_sum + 1)] for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1,n+1):
        for s in range(1,total_sum + 1):
            if arr[i-1] <= s:
                t[i][s] = t[i-1][s-arr[i-1]] + t[i-1][s]
            else:
                t[i][s] = t[i-1][s]
    return t[n][s]




def main():
    # Example values for the Subset Sum problem
    arr = [1 , 1 , 2 , 3]  # Set of numbers
    diff = 1  # Desired sum
    
    # Call the subset_sum function
    result = count_subset_difference(arr, diff)
    
    # Print the result
    print("Count of  subset with the given difference :", result)

if __name__ == "__main__":
    main()
