def print_mst(graph,parent,V):
    total_weight = 0
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
        total_weight += graph[i][parent[i]]  # Add edge weight to total

    print(f"Total weight of MST: {total_weight}")


def mininmun_key(key , v, mstset):
    min_index = -1
    min_value = float('inf')

    for u in range(v):
        if key[u] < min_value and not mstset[u]:
            min_value = key[u]
            min_index = u

    return min_index


def prims(graph,v):
    key = [float('inf')] * v 
    parent = [None] * v
    mstset = [False] * v
    parent[0] = -1
    key[0] = 0


    for _ in range(v):
        s = mininmun_key(key , v, mstset)
        mstset[s] = True

        for u in range(v):
            if (graph[s][u] > 0
                and not mstset[u] 
                and key[u] > graph[s][u]):
                key[u] = graph[s][u]
                parent[u] = s

    print_mst(graph,parent,v)




if __name__ == '__main__':
    V = 4
    graph = [[0, 5, 8, 0 ],
             [5, 0, 10, 15 ],
             [8, 10, 0, 20 ],
             [0, 15, 20, 0 ]]

    prims(graph, V)
                


