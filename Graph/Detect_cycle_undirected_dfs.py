from collections import deque  
def DFS(adj,s,visited,parent):
    visited[s] = True
    for u in adj[s]:
        if visited[u] == False:
            if DFS(adj,u,visited,s):
                return True
            
        elif u != parent:
            return True
        
    return False

def DFS_und(adj):
    visited=[False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            if DFS(adj,u,visited,-1):
                return True
            
    return False

def addEdge(adj,u,v):
    adj[v].append(u)
    adj[u].append(v)


v = 6 
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,1,2)
#addEdge(adj,2,3)
#addEdge(adj,0,2)
addEdge(adj,0,3)
addEdge(adj,4,5)

if(DFS_und(adj)):
    print("Cycle found")
else:
    print("No cycle")