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
        
        if distance[now] < dist:  # 이거 넣으니깐 time over 해결됨
             continue
        
        for next,weight in graph[now]:
            cost = dist + weight
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(queue,(cost,next))
    

dijkstra(start)
print(distance)  


#    if distance[now] < dist:  # 이거 넣으니깐 time over 해결도됨
#              continue
# 위 코드를 왜 넣는지 도저히 이해가 안감

# ChatGPT
# 위 코드에서 if distance[now] < dist: 부분은 Dijkstra 알고리즘의 핵심 부분 중 하나인데,
# 이 부분은 현재까지 발견한 최단 거리가 이미 기록된 거리보다 작을 때만 계산을 진행하도록 하는 역할을 합니다.
# 이 조건이 없으면 이미 발견한 노드의 거리보다 큰 값을 가진 노드들도 계속해서 우선순위 큐에 추가되어야 하므로 
# 시간 복잡도가 늘어나게 됩니다.

# 간단한 예를 들어 설명하면,

# 노드 A에서 B까지의 거리가 5로 기록되어 있음.
# 현재 우선순위 큐에 (4, B)가 있음.
# 그런데, 다음 노드인 B를 pop해서 꺼낼 때, 그 거리가 6이었다면, 이미 기록된 거리보다 크기 때문에 이를 무시하고 진행해야 합니다. 그렇지 않으면 불필요한 계산이 추가되어 시간이 낭비되게 됩니다.
# 따라서 if distance[now] < dist:는 이미 발견한 최단 거리보다 큰 값인 경우에는 무시하고 지나가도록 하는 역할을 합니다.





