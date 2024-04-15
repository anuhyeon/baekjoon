import sys
import heapq
n, k = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
S,X,Y = map(int,sys.stdin.readline().split())

nwes = [(1,0),(-1,0),(0,-1),(0,1)]
list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(list,(graph[i][j],i,j))

def bfs(G,list):
    global n, S
    q = []
    while list:
        k,x,y = heapq.heappop(list)
        for dx,dy in nwes:
            if 0<=x+dx<n and 0<=y+dy<n and G[x+dx][y+dy] == 0:
                G[x+dx][y+dy] = k
                heapq.heappush(q,(G[x+dx][y+dy],x+dx,y+dy))
    
                
    return q

for _ in range(S):
    list = bfs(graph,list)

print(graph[X-1][Y-1])