import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b =  map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
# print(graph)
def topo_sort_queue(G):
    global indegree
    answer = []
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        v = queue.popleft()
        answer.append(v)
        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    return answer


def topo_sort_stack(G): # DFS라고는 할 수 없으나 stack을 활요함.
    global indegree
    answer = []
    stack = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            stack.append(i)
    while stack:
        v = stack.pop()
        answer.append(v)
        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                stack.append(w)
    return answer


print(*topo_sort_queue(graph))

#print(*topo_sort_stack(graph))

# 6 5
# 1 2
# 2 3
# 4 3
# 5 3
# 6 5
#answer = [1, 4, 6, 2, 5, 3]
#answer = [6, 5, 4, 1, 2, 3]
