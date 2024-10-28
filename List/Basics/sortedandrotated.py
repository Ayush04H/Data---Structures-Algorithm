def checkRotatedAndSorted(arr,n):
    c = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            c+=1

    return c<=1


if __name__ == "__main__":
    arr = [9,10,11,12,13,14,15,1,2,3,4,5,6,7,8]  # Example array
    n = len(arr)
    
    if checkRotatedAndSorted(arr, n):
        print("The array is sorted and rotated.")
    else:
        print("The array is not sorted and rotated.")