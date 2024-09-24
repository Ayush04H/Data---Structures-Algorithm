def first_negative_in_window(arr, k):
    n = len(arr)
    i, j = 0, 0
    negatives = []  # List to store negative numbers in the current window
    result = []

    while j < n:
        # Add current element to negatives if it's negative
        if arr[j] < 0:
            negatives.append(arr[j])

        # If window size is smaller than k, just move the window forward
        if j - i + 1 < k:
            j += 1
        
        # Once window size equals k
        elif j - i + 1 == k:
            # If there are negative numbers, the first one is the result
            if negatives:
                result.append(negatives[0])
            else:
                result.append(0)  # If no negative number in the current window
            
            # Slide the window by removing the element at 'i' from the window
            if arr[i] < 0:
                negatives.pop(0)  # Remove the first negative if it's going out of the window

            # Move the window forward
            i += 1
            j += 1

    return result


# Example usage
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(first_negative_in_window(arr, k))
