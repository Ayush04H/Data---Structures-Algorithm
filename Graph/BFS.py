from collections import deque

def add_adj(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_list(adj):
    for u,v in enumerate(adj):
        print(u,v)
    
def bfs(adj):
    s=0
    q=deque()
    q.append(s)
    visited = [False] * len(adj)
    visited[s]=True 
    while q:
        s=q.popleft()
        print(s,end=" ")
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u]=True


v=6
adj=[[] for i in range(v)]
add_adj(adj,0,1)
add_adj(adj,0,2)
add_adj(adj,0,5)
add_adj(adj,1,3)
add_adj(adj,3,5)
add_adj(adj,4,5)
add_adj(adj,2,4)

print_list(adj)
bfs(adj)

