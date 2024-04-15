import sys
import heapq
n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append((b,1))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue,(0,start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        for next,w in graph[now]:
            cost = dist + w   #distance[now]
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue,(cost,next))

dijkstra(x)
# print(distance)
cnt = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        cnt += 1
if cnt == 0:
        print(-1)
    