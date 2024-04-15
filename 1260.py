import sys
n, m, v = map(int,sys.stdin.readline().split())
# print(n,m,v)

graph = [[] for _ in range(n+1)]
# print(graph)
for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

#print(graph)

for i in range(len(graph)):
   graph[i] = sorted(graph[i]) 

#print(graph)


def DFS(graph,start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in reversed(graph[v]):
                stack.append(w)
            

    return visited

def BFS(graph,start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    
    return visited
    

print(*DFS(graph,v))
print(*BFS(graph,v))