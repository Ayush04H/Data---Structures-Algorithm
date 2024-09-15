def dfs_rec(adj,s,visited,recst):
    visited[s] = True
    recst[s] = True

    for u in adj[s]:
        if visited[u] == False and dfs_rec(adj,u,visited,recst):
            return True
        
        elif recst[u] == True:
            return True
        
    recst[s] = False
    return False

def dfs(adj,v):
    if v == 1 or v == 0:
        return False
        
    visited = [False] * v
    recst = [False] * v

    for u in range(v):
        if visited[u] == False:
            if dfs_rec(adj,u,visited,recst):
                return True
            
    return False


def main():
    # Number of vertices
    v = 4

    # Adjacency list of the directed graph
    adj = [[] for _ in range(v)]
    
    # Sample graph edges (directed graph)
    adj[0].append(1)
    adj[1].append(2)  # This creates a cycle: 0 -> 1 -> 2 -> 0
    adj[2].append(0)

    # Call dfs function to detect cycle
    if dfs(adj, v):
        print("Cycle detected")
    else:
        print("No cycle detected")

# Call the main function
if __name__ == "__main__":
    main()