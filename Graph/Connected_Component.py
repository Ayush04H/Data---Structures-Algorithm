from collections import deque
def bfs(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True 
    while q:
        s=q.popleft()
        for u in adj[s]:
            if visited[u]==False:
                q.append(u)
                visited[u]=True


def bfs_dis(adj):
    visited = [False]*len(adj)
    res=0
    for u in range(len(adj)):
        if visited[u]== False:
            bfs(adj,u,visited)
            res+=1
    print("The Connected Components are :",res)

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


v = 10

adj = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5] , [8,9] , [7,9] ,[7,8]]
printGraph(adj)
print('\nBFS path')
bfs_dis(adj)