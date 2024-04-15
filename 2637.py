import sys
from collections import deque
from copy import deepcopy

n = int(sys.stdin.readline().rstrip()) # 노드개수
m = int(sys.stdin.readline().rstrip()) 
graph = [[] for _ in range(n+1)] #[가리키는 노드, 가리키는 노드를 만들기 위한 부품개수] ex) graph[1][0] : 1번 부품이 가리키는 부품, graph[1][1]: 자신(1번)이 가리키는 부품을 만들기 위해서 자신이 몇개가 필요한지
indegree = [[]for _ in range(n+1)]
k_info = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,k = map(int,sys.stdin.readline().split()) # 부품 x를 만드는데 부품 y가 k개 필요하다.
    graph[y].append((x,k)) # y: 자신노드, x: 가리키는 노드, k: 가리키는 노드를 만들기 위해서 자신이 몇개 필요한지.
    indegree[x].append(y)
    k_info[x][y] += k
_indegree =  deepcopy(indegree)
#print(k_info)
#print("fisrt: ",_indegree)   
def topology_sort(G):
    answer = []
    queue = deque()
    for i in range(1,n):
        if indegree[i] == []:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        answer.append(now)
        for next,_ in G[now]:
            indegree[next].remove(now)
            if indegree[next] == []:
                queue.append(next)
    
    return answer
answer = topology_sort(graph)
#print(answer)
#print("second:",indegree)

for i in reversed(answer):
    if graph[i] == []:
        continue
    sum = 0
    for row in k_info:
        sum += row[i]
    
    for j in range(n+1):
        k_info[i][j] *= sum
             
#print(k_info)

for i in range(1,n+1):
    if _indegree[i] == []:
        total = 0
        for row in k_info:
           total += row[i]
        print(i,total)
        
    
        
# [[], [], [], [], [], [1, 2], [5, 3, 4], [5, 6, 4]]
#[[], [(5, 2)], [(5, 2)], [(6, 3)], [(6, 4), (7, 5)], [(7, 2), (6, 2)], [(7, 3)], []]
    #0  1  2  3  4  5  6  7 
# 0[[0, 0, 0, 0, 0, 0, 0, 0],
# 1 [0, 0, 0, 0, 0, 0, 0, 0],
# 2 [0, 0, 0, 0, 0, 0, 0, 0],
# 3 [0, 0, 0, 0, 0, 0, 0, 0],
# 4 [0, 0, 0, 0, 0, 0, 0, 0],
# 5 [0, 2, 2, 0, 0, 0, 0, 0],
# 6 [0, 0, 0, 3, 4, 2, 0, 0],
# 7 [0, 0, 0, 0, 5, 2, 3, 0]]


# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 16, 16, 0, 0, 0, 0, 0],
#  [0, 0, 0, 9, 12, 6, 0, 0],
#  [0, 0, 0, 0, 5, 2, 3, 0]]