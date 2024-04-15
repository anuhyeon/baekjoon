import sys
import heapq
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
INF = int(1e9)
graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
start, end = map(int,sys.stdin.readline().split())
#print(graph)

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue,(0,start))
    
    
    while queue: 
        dist,now = heapq.heappop(queue)
        
        if distance[now] < dist:
             continue
        
        for next,weight in graph[now]:
            cost = dist + weight
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(queue,(cost,next))
    

dijkstra(start)
print(distance[end])  