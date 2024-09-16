from collections import deque
def bfs(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True 
    while q:
        s=q.popleft()
        print(s,end=" ")
        for u in adj[s]:
            if visited[u]==False:
                q.append(u)
                visited[u]=True


def bfs_dis(adj):
    visited = [False]*len(adj)
    for u in range(len(adj)):
        if visited[u]== False:
            bfs(adj,u,visited)

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)

def add_adj(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_list(adj):
    for u,v in enumerate(adj):
        print(u,v)

v=4
adj=[[] for i in range(v)]
add_adj(adj,0,1)
add_adj(adj,0,3)
add_adj(adj,1,2)
add_adj(adj,1,3)
add_adj(adj,3,2)
print_list(adj)

print('\nBFS path')
bfs_dis(adj)