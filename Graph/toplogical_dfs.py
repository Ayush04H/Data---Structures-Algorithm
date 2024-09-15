def add_node(adj, u, v):
    adj[u].append(v)

def print_node(adj):
    for u, l in enumerate(adj):
        print(u, l)

def dfs_rec(adj, s, visited, stack):
    visited[s] = True
    # Explore all the adjacent nodes of `s`
    for u in adj[s]:
        if not visited[u]:
            dfs_rec(adj, u, visited, stack)
    # Push current node to the stack after all its neighbors are processed
    stack.append(s)

def dfs_topo(adj, v):
    visited = [False] * v
    stack = []
    for u in range(v):
        if not visited[u]:
            dfs_rec(adj, u, visited, stack)
    
    # Reverse the stack to get the topological order
    stack.reverse()
    
    return stack

# Example usage
v = 6
adj = [[] for i in range(v)]

add_node(adj, 0, 1)
add_node(adj, 0, 2)
add_node(adj, 1, 3)
add_node(adj, 2, 3)
add_node(adj, 3, 4)
add_node(adj, 3, 5)

print_node(adj)
print(dfs_topo(adj, v))
