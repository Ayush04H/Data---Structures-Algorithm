def dfs_rec(adj,s,visited,colour):
    if visited[s] !=0:
        return visited[s] == colour
    visited[s] = colour

    for u in adj[s]:
        if not dfs_rec(adj,u,visited,-colour):
            return False
    return True

def dfs(adj):
    n = len(adj)
    visited = [0] * n

    for u in range(n):
        if visited[u] == 0:
            if not dfs_rec(adj,u,visited,-1):
                return False
        
    return True


graph = [[1,3],[0,2],[1,3],[0,2]]
print(dfs(graph))