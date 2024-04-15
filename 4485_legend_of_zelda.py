import sys
import heapq

nwes = [(1,0),(-1,0),(0,-1),(0,1)]

def dijkstra(G):
    q = []
    #print(G)
    heapq.heappush(q,(G[0][0],0,0))
    visited[0][0] = 1
    while q:
        cost,x,y = heapq.heappop(q)
        if x == len(G)-1 and y == len(G[0]) - 1:
            return cost
        for dx,dy in nwes:
            if 0<=x+dx<len(G) and 0<=y+dy<len(G[0]) and visited[x+dx][y+dy] == 0:
                visited[x+dx][y+dy] = 1
                new_cost = cost + G[x+dx][y+dy]
                heapq.heappush(q,(new_cost,x+dx,y+dy)) 
        

n = 1
res = []
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    res.append(dijkstra(graph))
  
#print(res)
for i in range(len(res)):
    print(f'Problem {i+1}: {res[i]}')
    
    
# n = int(sys.stdin.readline().rstrip())
# graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]
# print(dijkstra(graph))