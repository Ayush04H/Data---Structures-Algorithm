import math 
from collections import deque 
MAX=999999
def addEdge(adj,u,v):
    adj[v].append(u)
    adj[u].append(v)

def bfs(adj,s,dis):
    visited=[False] * len(adj)
    q=deque()
    visited[s]=True
    q.append(s)
    while q:
        u=q.popleft()
        for v in adj[u]:
            if visited[v]==False:
                dis[v]=dis[u] + 1
                visited[v]=True 
                q.append(v)

v = 4 
adj = [[] for i in range(v)]

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)

addEdge(adj,0,1)
addEdge(adj,1,2)
addEdge(adj,1,3)
addEdge(adj,2,3)
addEdge(adj,0,2)

printGraph(adj)
dist =[MAX]*v
dist[0]=0
bfs(adj,0,dist)

print(*dist)
