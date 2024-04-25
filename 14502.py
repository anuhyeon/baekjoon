import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
copied_graph = [[0]*m for _ in range(n)]
urld = [(1, 0), (0, 1), (-1, 0), (0, -1)]
max_area = 0  # 최대 영역 크기를 저장할 변수 이름 변경

def bfs():
    global max_area
    q = deque()
    # 그래프 초가화
    for i in range(n):
        for j in range(m):
            copied_graph[i][j] = graph[i][j]    
    # 전염병있는 곳 큐에 저장     
    for i in range(n):
        for j in range(m):
            if copied_graph[i][j] == 2:
                q.append((i, j))
    # 전염시키기
    while q:
        x, y = q.popleft()
        for dx, dy in urld:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and copied_graph[nx][ny] == 0:
                copied_graph[nx][ny] = 2
                q.append((nx, ny))

    #count = sum(row.count(0) for row in copied_graph)
    ##안전영역 너비 계산
    count = 0            
    for i in range(n):
        for j in range(m):
            if copied_graph[i][j] == 0:
                count += 1
    if max_area < count:
        max_area = count

def dfs(cnt):
    if cnt == 3:
        bfs()  # 벽을 세운 후 바이러스 퍼트리기
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0  # 다시 벽을 없애기

dfs(0)
print(max_area)




# import sys
# from collections import deque
# import copy
# n, m = map(int,sys.stdin.readline().split())
# tmp_graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# #tmp_graph = copy.deepcopy(graph)
# visited_dfs = [[0]*m for _ in range(n)]

# urld = [(1,0),(0,1),(-1,0),(0,-1)]
# max = 0
        
# def bfs():
#     global max
#     graph = copy.deepcopy(tmp_graph)
#     q = deque()
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 2:
#                 q.append((i,j))
    
#     while q:
#         x,y = q.popleft()
#         for dx,dy in urld:
#             if 0<=x+dx<n and 0<=y+dy<m and graph[x+dx][y+dy] == 0:
#                 graph[x+dx][y+dy] = 2
#                 q.append((x+dx,y+dy))
    
#     count = 0            
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 count += 1
    
#     if max < count:
#         max = count


# def dfs(cnt):  # 벽 세우기 --> 조합 
#     global graph, tmp_graph, visited_bfs
#     if cnt == 3:
#         bfs()
#         return
    
#     for i in range(n):
#         for j in range(m):
#             if tmp_graph[i][j] == 0 and visited_dfs[i][j] == 0:
#                 tmp_graph[i][j] = 1
#                 visited_dfs[i][j] = 1
#                 dfs(cnt+1)
#                 tmp_graph[i][j] = 0
#                 visited_dfs[i][j] = 0
                

# dfs(0)
# print(max)
    
# 0 0 0 1 0 0
# 1 0 0 1 0 2
# 1 1 1 0 0 2
# 0 0 0 1 0 2 

# [[0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 2],
#  [1, 1, 1, 0, 0, 2],
#  [0, 0, 0, 0, 0, 2]]

# [[2, 2, 2, 1, 2, 2],
#  [1, 2, 2, 1, 2, 2],
#  [1, 1, 1, 2, 2, 2],
#  [0, 0, 0, 1, 2, 2]]