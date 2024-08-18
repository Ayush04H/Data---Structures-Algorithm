from collections import defaultdict, deque

def add_edge(graph, u, v, w):
    graph[u].append((v, w))

def topological_sort_util(v, visited, stack, graph):
    visited[v] = True

    for node, weight in graph[v]:
        if not visited[node]:
            topological_sort_util(node, visited, stack, graph)

    stack.append(v)

def shortest_path(graph, V, s):
    visited = [False] * V
    stack = deque()

    for i in range(V):
        if not visited[i]:
            topological_sort_util(s, visited, stack, graph)

    dist = [float("Inf")] * V
    dist[s] = 0

    while stack:
        i = stack.pop()
        
        for node, weight in graph[i]:
            if dist[node] > dist[i] + weight:
                dist[node] = dist[i] + weight

    for i in range(V):
        print(f"{dist[i] if dist[i] != float('Inf') else 'Inf'}", end=" ")

# Number of vertices
V = 6

# Create a graph as a defaultdict of lists
graph = defaultdict(list)

# Add edges
add_edge(graph, 0, 1, 5)
add_edge(graph, 0, 2, 3)
add_edge(graph, 1, 3, 6)
add_edge(graph, 1, 2, 2)
add_edge(graph, 2, 4, 4)
add_edge(graph, 2, 5, 2)
add_edge(graph, 2, 3, 7)
add_edge(graph, 3, 4, -1)
add_edge(graph, 4, 5, -2)

# Source
s = 1

print(f"Following are shortest distances from source {s}")
shortest_path(graph, V, s)
