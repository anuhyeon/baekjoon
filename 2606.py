import sys

def DFS(G,start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in G[v]:
                stack.append(w)
                
    return visited

def BFS(G,start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in G[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

print(len(DFS(graph,1))-1)
#print(*BFS(graph,1))