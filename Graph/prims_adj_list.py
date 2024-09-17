def minimum_key(key, V, mstset):
    min_index = -1
    min_value = float('inf')

    for u in range(V):
        if key[u] < min_value and not mstset[u]:
            min_value = key[u]
            min_index = u

    return min_index

def prims(graph, V):
    key = [float('inf')] * V
    mstset = [False] * V
    key[0] = 0
    res = 0

    for _ in range(V):
        u = minimum_key(key, V, mstset)
        mstset[u] = True

        res += key[u]

        # Iterate over the adjacency list for the vertex `u`
        for (s, weight) in graph[u]:
            if not mstset[s] and weight != 0 and weight < key[s]:
                key[s] = weight

    return res

if __name__ == '__main__':
    V = 4
    graph = [[] for _ in range(V)]
    graph[0].append((1, 5))
    graph[0].append((2, 8))
    graph[1].append((0, 5))
    graph[1].append((2, 10))
    graph[1].append((3, 15))
    graph[2].append((0, 8))
    graph[2].append((1, 10))
    graph[2].append((3, 20))
    graph[3].append((1, 15))
    graph[3].append((2, 20))
    
    result = prims(graph, V)
    print("Total weight of the minimum spanning tree:", result)
