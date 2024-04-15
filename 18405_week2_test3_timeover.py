import sys
from collections import deque
import heapq

n,k = map(int,sys.stdin.readline().split())

nwes = [(1,0),(-1,0),(0,-1),(0,1)]
visited = [[0]*n for _ in range(n)]
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

S,X,Y = map(int,sys.stdin.readline().split())

list = []

for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                heapq.heappush(list,(graph[i][j],i,j))
            
def bfs(G,x,y):
    global list, visited
    q = deque()
    q.append((G[x][y],x,y))
    visited[x][y] = 1
    k,x,y = q.popleft()

    for dx,dy in nwes:
        if 0<=x+dx<len(G) and 0<=y+dy<len(G[0]) and visited[x+dx][y+dy] == 0 and G[x+dx][y+dy]==0:
            visited[x+dx][y+dy] = 1
            G[x+dx][y+dy] = k
            q.append((G[x+dx][y+dy],x+dx,y+dy))
            #heapq.heappush(list,(G[x+dx][y+dy],x+dx,y+dy))
            

def solution(G):
    global n,list,S,X,Y
    for _ in range(S):
        for _ in range(len(list)):
            _,x,y = heapq.heappop(list)
            bfs(G,x,y)
            heapq.heappush() 
        for i in range(n):
            for j in range(n):
                if G[i][j] != 0:
                    heapq.heappush(list,(G[i][j],i,j))
        print(G) #그래프 생성과정 출력
    
    print(G[X-1][Y-1])
      
solution(graph)    