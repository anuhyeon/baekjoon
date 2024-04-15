import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))  

distance = [int(1e9)]*(n+1)

def dijkstra(G,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue      
        for next,weight in G[now]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))

dijkstra(graph,k)
#print(distance)

for i in range(1,n+1):
    if distance[i] == int(1e9):
        print('INF')
    else:
        print(distance[i])