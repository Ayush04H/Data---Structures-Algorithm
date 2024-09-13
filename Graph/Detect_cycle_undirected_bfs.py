from collections import deque

# Function to perform BFS and detect a cycle in an undirected graph 
def BFS_cycle_detection(adj, s, visited,parent):
    # Queue will store pairs (node, parent)
    q = deque()
    q.append(s)
    visited[s] = True
    
    # BFS loop
    while q:
        node = q.popleft() # O(v+e) , O(v)
        
        # Visit all adjacent nodes
        for u in adj[node]:
            if not visited[u]:
                visited[u] = True
                q.append((u))
            elif u != parent:
                # If an adjacent node is visited and it's not the parent, a cycle exists
                return True
    
    return False

# Function to check if the graph has a cycle using BFS
def BFS_undirected_cycle(adj, V):
    visited = [False] * V
    
    # Loop through all vertices to ensure all components are checked 
    for u in range(V):
        if not visited[u]:
            if BFS_cycle_detection(adj, u, visited,-1):
                return True
            
    return False

# Helper function to add edges to the adjacency list 
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)    # O(v+e) , O(v)

# Example usage
v = 6
adj = [[] for i in range(v)]

addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
# addEdge(adj, 2, 3)
# addEdge(adj, 0, 2)
addEdge(adj, 0, 3)
addEdge(adj, 4, 5)

# Checking if a cycle exists in the graph using BFS
if BFS_undirected_cycle(adj, v):
    print("Cycle found")
else:
    print("No cycle")



# Dry Rnun For The above  is 