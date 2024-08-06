def add_adj(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)


def DFS(adj,s,visited):
    visited[s] = True

    print(s, end=' ')

    for u in adj[s]:

        if visited[u] == False:
            DFS(adj, u, visited)

def DFS_rec(adj,s):
    visited=[False] * len(adj) 
    DFS(adj,s,visited)

def print_list(adj):
    for u,v in enumerate(adj):
        print(u,v)


v=5
adj=[[] for i in range(v)]
add_adj(adj,0,1)
add_adj(adj,0,4)
add_adj(adj,1,4)
add_adj(adj,1,3)
add_adj(adj,1,2)
add_adj(adj,2,3)
add_adj(adj,4,3)

print_list(adj)
DFS_rec(adj,0)