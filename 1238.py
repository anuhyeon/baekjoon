import sys
import heapq

n,m,x = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append((b,t))
#print(graph)

def dijkstra(G,start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [int(1e9)]*(len(G))
    #import pdb; pdb.set_trace()
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            return distance   
        for next, w in G[now]:
            cost = dist + w
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    
    return distance

result = dijkstra(graph,x)
result[0] = -1
#print(result)
for i in range(1,n+1):
    if i == x:
        continue
    result[i] += dijkstra(graph,i)[x]

print(max(result))
        

# result = [0]*(n+1) #for _ in range(n+1)
# for i in range(1,n+1):
#     distance = [int(1e9)]*(n+1)
#     if i == x:
#         dijkstra(graph,i)
#         for j in range(1,n+1):
#             result[j] = distance[j]
#     dijkstra(graph,i)
#     result[i] += distance[x]
    
# print(result)
    
    
    