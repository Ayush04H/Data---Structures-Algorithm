'''def linear(arr,ind,x):
    if ind == len(arr):
        return -1
    if arr[ind] == x:
        return ind

    
    return linear(arr,ind+1,x)'''



'''def linear(arr, ind, x, indices=None):
    if indices is None:
        indices = []  # Initialize indices list if not already passed
    
    if ind == len(arr):
        return indices  # Return all collected indices

    if arr[ind] == x:
        indices.append(ind)  # Add the current index to the list of indices

    return linear(arr, ind + 1, x, indices)  # Recursively search the next index'''



def linear(arr,ind,x):
    if ind == len(arr):
        return []
    res = linear(arr,ind+1,x)

    if arr[ind] == x:
        return [ind] + res

    return res

arr = [1, 2, 3, 4, 5, 6, 8, 4]
print(linear(arr, 0, 4))  # Output: [3, 7]


