def print_mst(parent, graph, V):
    total_weight = 0
    print("Edge \tWeight")
    for i in range(1, V):
        u = parent[i]
        v = i
        # Find the weight of the edge u-v in the adjacency list
        weight = next(weight for node, weight in graph[u] if node == v)
        print(f"{u} - {v} \t {weight}")
        total_weight += weight

    print(f"Total weight of MST: {total_weight}")

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
    parent = [None] * V
    mstset = [False] * V
    parent[0] = -1
    key[0] = 0

    for _ in range(V):
        u = minimum_key(key, V, mstset)
        mstset[u] = True

        for v, weight in graph[u]:
            if not mstset[v] and key[v] > weight:
                key[v] = weight
                parent[v] = u

    print_mst(parent, graph, V)

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

    prims(graph, V)
