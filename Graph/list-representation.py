def add_adj(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printadj(adj):
    for u,l in enumerate(adj):
        print(u,l)

v=5
adj=[[] for i in range(v)]
add_adj(adj,0,1)
add_adj(adj,0,4)
add_adj(adj,1,4)
add_adj(adj,1,3)
add_adj(adj,1,2)
add_adj(adj,2,3)
add_adj(adj,4,3)

printadj(adj)