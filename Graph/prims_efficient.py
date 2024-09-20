import heapq
def prims(graph,v):
    key = [float('inf')] * v
    mstset = [False] * v
    key[0] = 0

    min_heap = [(0,0)]
    res = 0

    while min_heap:
        curr_key , u = heapq.heappop(min_heap)
        if mstset[u]:
            continue
        mstset[u] = True
        res += curr_key


        for (s,weight) in graph[u]:
            if not mstset[s] and weight != 0 and weight < key[s]:
                key[s] = weight

                heapq.heappush(min_heap,(weight,s))

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

