import sys
import copy
def DFS(graph,start):
    global visited 
    stack = [start]
    while stack:
        v = stack.pop() # v에 방문할 예정 입밎다~
        if v not in visited: # v에 방문 한적 있나요?
            visited.append(v) # 방문한 적 없으면 v에 방문도장
            for w in reversed(graph[v]):
                stack.append(w)
                
    return visited

def BFS(graph,start):
    global visited
    visited.append(start)
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    
#print(graph)

visited = []
DFS(graph,1)
updated_visited = copy.deepcopy(visited)
#print(visited)

cnt = 1
for i in range(1,n+1):
     if i not in updated_visited:
         updated_visited +=DFS(graph,i)
         cnt += 1
print(cnt)   