from collections import deque
def add_node(adj,u,v):
    adj[u].append(v)

def print_node(adj):
    for i,j in enumerate(adj):
        print(i,j)


def topological_sort(adj,v):
    indegree = [0]*v
    for i in range(v):
        for u in adj[i]:
            indegree[u]+=1

    q = deque()

    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    top = []
    count = 0

    while q:
        s = q.popleft()
        top.append(s)

        for u in adj[s]:
            indegree[u]-=1
            if indegree[u] == 0:
                q.append(u)


        count +=1

    if count != v:
        return True
    else:
        return False


v = 6
adj = [[] for i in range(v)]

add_node(adj,0,1)
add_node(adj,2,0)
add_node(adj,1,3)
add_node(adj,3,2)
add_node(adj,3,4)
add_node(adj,5,3)



print_node(adj)
print(topological_sort(adj,v))