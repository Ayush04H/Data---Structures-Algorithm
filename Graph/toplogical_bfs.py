from collections import deque

def add_node(adj,u,v):
    adj[u].append(v)

def topological_sort(adj,v):
    if v==0 or v==1:
        return v
    
    indegree = [0]*v
    for i in range(v):
        for u in adj[i]:
            indegree[u] +=1

    q = deque()

    for i in range(v):
        if indegree[i] == 0:
            q.append(i)


    top = []
    count = 0

    while q:
        s=q.popleft()
        top.append(s)
        for u in adj[s]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)

        count+=1

    if count != v:
        return []
    
    return top
      

def print_ele(adj):
    for u,l in enumerate(adj):
        print(u,l)

v = 6
adj = [[] for i in range(v)]

add_node(adj,0,1)
add_node(adj,0,2)
add_node(adj,1,3)
add_node(adj,2,3)
add_node(adj,3,4)
add_node(adj,3,5)



print_ele(adj)
print(topological_sort(adj,v))