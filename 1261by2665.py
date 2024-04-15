# 단순히 시작 지점 [0][0] -> 끝 지점 [n-1][n-1]으로의 최단경로는 BFS로 해결 가능.
# 하지만, 방을 바꾸는 최소 개수에 해당하는 경로는 최단경로가 아닐 수 있음

# 시작 지점으로부터 나머지 모든 지점으로 갈 때, 방을 바꾸는 최소 개수 (최소 비용)=> 다익스트라

#BFS로 도착지점까지 가는 도중 검정색 벽을 만나는 횟수를 구하면 되는 겨?
import sys
import heapq
n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(m)]
#print(graph)
visited = [[0]*n for _ in range(m)]
nwes = [(1,0),(-1,0),(0,-1),(0,1)]
#print(graph)
def dijkstra_bfs(G):
    #import pdb; pdb.set_trace()
    q = []
    visited[0][0] = 1
    heapq.heappush(q,(0,0,0)) # 0,0,0 = cnt,x,y
    while q:
        cost,x,y = heapq.heappop(q)
        if x == m-1 and y == n-1 :
            return cost
        for dx,dy in nwes:
            if 0<=x+dx<m and 0<=y+dy<n and visited[x+dx][y+dy] == 0:
                visited[x+dx][y+dy] = 1
                if G[dx+x][dy+y] == 1: # 벽일경우
                    heapq.heappush(q,(cost+1,x+dx,y+dy))
                else:
                    heapq.heappush(q,(cost,x+dx,y+dy))

print(dijkstra_bfs(graph))
        
    
