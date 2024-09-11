from collections import deque

# Function to find the level of node X in a graph
def levelOfX(V, adj, X):
    # Initialize the queue for BFS
    q = deque()
    
    # Array to keep track of visited nodes
    visited = [False] * V
    
    # Array to store levels of each node
    level = [-1] * V
    
    # Start BFS from node 0
    visited[0] = True
    level[0] = 0
    q.append(0)
    
    # BFS loop
    while q:
        s = q.popleft()
        
        # Visit all adjacent nodes
        for u in adj[s]:
            if not visited[u]:
                level[u] = level[s] + 1
                visited[u] = True
                q.append(u)
                
                # If we find node X, return its level
                if u == X:
                    return level[u]
    
    # If node X is not found, return 0
    return 0

# Main function to set up the graph and call levelOfX
if __name__ == "__main__":
    # Number of vertices in the graph
    V = 6
    
    # Initialize an adjacency list for the graph
    adj = [[] for _ in range(V)]
    
    # Helper function to add edges to the adjacency list
    def add_adj(adj, u, v):
        adj[u].append(v)
        adj[v].append(u)

    # Example graph edges
    add_adj(adj, 0, 1)
    add_adj(adj, 0, 2)
    add_adj(adj, 1, 3)
    add_adj(adj, 2, 4)
    add_adj(adj, 3, 4)
    add_adj(adj, 3, 5)

    # Node X to find the level of
    X = 5

    # Call the function and print the level of node X
    level = levelOfX(V, adj, X)
    print(f"Level of node {X} is {level}")
