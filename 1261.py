import sys
import heapq

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(m)]
##print(graph)
visited = [[0]*n for _ in range(m)]
nsew = [(1,0),(-1,0),(0,-1),(0,1)]
##print(visited)
def dijkstra(G):
    global n,m
    q = []
    visited[0][0] = 1
    heapq.heappush(q,(0,0,0))
    while q:
        cost,i,j = heapq.heappop(q)
        if i == m-1 and j == n-1:
            return cost
        for di,dj in nsew:
            if 0<=i+di<m and 0<=j+dj<n and visited[i+di][j+dj] == 0:
                visited[i+di][j+dj] = 1
                if G[i+di][j+dj] == 1:
                    heapq.heappush(q,(cost+1,i+di,j+dj))
                else:
                    heapq.heappush(q,(cost,i+di,j+dj))

print(dijkstra(graph))
    
    