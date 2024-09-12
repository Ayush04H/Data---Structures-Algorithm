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


''' DRY RUN WITH EXAMPLE

        V = 6
        adj = [[1, 3], [0, 2], [1], [0, 4], [3, 5], [4]]

        Step-by-Step Dry Run:
        Initial Setup:

        visited = [False, False, False, False, False, False]
        Start DFS from node 0.
        DFS on Node 0:

        Mark 0 as visited: visited = [True, False, False, False, False, False].
        Check adjacent nodes of 0: nodes 1 and 3.
        DFS on Node 1:

        Mark 1 as visited: visited = [True, True, False, False, False, False].
        Check adjacent nodes of 1: nodes 0 and 2.
        Node 0 is the parent, so skip it.
        Move to node 2.
        DFS on Node 2:

        Mark 2 as visited: visited = [True, True, True, False, False, False].
        Check adjacent node of 2: node 1 (parent), so return False.
        No cycle found in this branch.
        Backtrack to Node 0, DFS on Node 3:

        Mark 3 as visited: visited = [True, True, True, True, False, False].
        Check adjacent nodes of 3: nodes 0 and 4.
        Node 0 is the parent, so skip it.
        Move to node 4.
        DFS on Node 4:

        Mark 4 as visited: visited = [True, True, True, True, True, False].
        Check adjacent nodes of 4: nodes 3 and 5.
        Node 3 is the parent, so skip it.
        Move to node 5.
        DFS on Node 5:

        Mark 5 as visited: visited = [True, True, True, True, True, True].
        Check adjacent node of 5: node 4 (parent), so return False.
        No cycle found.
'''