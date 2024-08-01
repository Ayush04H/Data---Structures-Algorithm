def find_rank_in_stream(stream, key):
    count = 0
    for element in stream:
        if element <= key:
            count += 1
    return count - 1

# Driver code 
if __name__ == '__main__':
    a = [5, 1, 4, 4, 5, 9, 7, 13, 3] 
    key = 4
    rank = find_rank_in_stream(a, key)
    print("Rank of", key, "in stream is:", rank)
