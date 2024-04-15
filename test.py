# import heapq

# def dijkstra(s):
#     D = [float('inf')] * (N+1)
#     D[s] = 0
#     q = []								    # 최단 거리 테이블을 heap으로 구현
#     heapq.heappush(q, (0, s))				# heap에 (가중치, 노드) 형식으로 삽입 
#     while q:
#         dist, now = heapq.heappop(q)		# 최소힙이므로 가중치가 가장 작은 값이 pop
#         if D[now] >= dist:					# 이미 최솟값 구했는지 확인
#             for v, val in city[now]:		# 연결된 노드들 확인
#                 if dist + val < D[v]:		# 가중치가 더 작은 값이면 갱신
#                     D[v] = dist + val
#                     heapq.heappush(q, (dist + val, v))
#     return D

# N, M, X = map(int, input().split())
# city = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b, t = map(int, input().split())
#     city[a].append([b, t])
# ans = dijkstra(X)
# ans[0] = 0
# for i in range(1, N+1):
#     if i != X:
#         res = dijkstra(i)
#         ans[i] += res[X]

# print(max(ans))
# print(ans)


# import sys
# import heapq

# n,m,x = map(int,sys.stdin.readline().split())
# graph = [[]for _ in range(n+1)]

# for _ in range(m):
#     a,b,t = map(int,sys.stdin.readline().split())
#     graph[a].append((b,t))

# def dijkstra(G,start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance = [int(1e9)]*(len(G))
#     #import pdb; pdb.set_trace()
#     distance[start] = 0
#     while q:
#         dist,now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue  
#         for next, w in G[now]:
#             cost = dist + w
#             if cost < distance[next]:
#                 distance[next] = cost
#                 heapq.heappush(q,(cost,next))
    
#     return distance

# result = dijkstra(graph,x)
# result[0] = 0

# for i in range(1,n+1):
#     if i != x:
#         result[i] += dijkstra(graph,i)[x]

# print(max(result))
# #print(result)      

# import sys
# import heapq

# n, m = map(int,sys.stdin.readline().split())
# graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(m)]
# print(graph)
# visited = [[0]*n for _ in range(m)]
# nsew = [(1,0),(-1,0),(0,-1),(0,1)]
# print(visited)
# def dijkstra(G):
#     global n,m
#     q = []
#     heapq.heappush(q,(0,0,0))
#     visited[0][0] = 1
#     while q:
#         cost, i, j = heapq.heappop(q)
#         if i == m-1 and j == n-1:
#             return cost
#         for di,dj in nsew:
#             if 0<=i+di<m and 0<=j+dj<n and visited[i+di][j+dj] == 0:
#                 visited[i+di][j+dj] == 1
#                 if G[i+di][j+dj] == 1:
#                     heapq.heappush(q,(cost+1,i+di,j+dj))
#                 else:
#                     heapq.heappush(q,(cost,i+di,j+dj))

# print(dijkstra(graph))

# def dfs(x, y):
#     visited[x][y] = True
#     if array[x][y] == '|' :
#         if x+1<n and array[x+1][y] == '|' and visited[x+1][y]==False:
#             dfs(x+1, y)
#         else:
#             return
#     if array[x][y] == '-' :
#         if y+1<m and array[x][y+1] == '-' and visited[x][y+1]==False:
#             dfs(x, y+1)
#         else:
#             return
    

# n, m = map(int, input().split())
# array = []
# count = 0

# # 리스트의 얕은 복사
# visited = []
# temp = [False]*m
# for _ in range(n):
#     visited.append(temp[:])

# for _ in range(n):
#     array.append(list(input()))
        
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == False:
#             dfs(i, j)
#             count+=1
# print(count)

# import sys
# import heapq
# from collections import deque
# n = int(sys.stdin.readline().rstrip())

# graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
# nwes = [(1,0),(-1,0),(0,-1),(0,1)]
# visited = [[0]*n for _ in range(n)]
# cnt = 0
# a = 0
# def dfs_recurs(G,i,j,visited):
#     visited[i][j] = 1
#     a = 0
#     for di,dj in nwes:
#         if  0 <= i+di < len(G) and 0 <= j+dj < len(G[0]) and G[i+di][j+dj] == 1 and visited[i+di][j+dj] == 0:
#             dfs_recurs(G,i+di,j+dj,visited)
#             a += 1
#     print(a)
# #def dfs_stack(G):

# def solution(G,visited):
#     global cnt
#     for x in range(len(G)):
#         for y in range(len(G[0])):
#             if G[x][y] != 0 and visited[x][y] == 0:
#                 dfs_recurs(G,x,y,visited)
#                 cnt += 1

#     return cnt

# print(solution(graph,visited))
# print()
# print(visited)

    
# exp = input().split('-') #'-'를 기준으로 split해서 exp 리스트에 저장

# num = [] #'-'로 나눈 항들의 합을 저장할 리스트

# for i in exp:
#     sum = 0
#     tmp = i.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
#     for j in tmp: #split한 리스트의 각 요소들을 더해줌
#         sum += int(j)
#     num.append(sum) #각 항의 연산 결과(덧셈)를 num에 저장

# n = num[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

# for i in range(1,len(num)): #1번째 값부터 n에서 빼준다
#     n -= num[i]







# N, K = map(int, input().split())
# if N >= K :
#   print(0)
#   exit()

# elec_list = list(map(int, input().split()))

# plug = set()
# cnt = 0

# def find_latest(idx) :
#   result = 0
#   max_idx = -1
#   for num in plug :
#     try :
#       num_idx = elec_list[idx:].index(num)
#     except :
#       num_idx = K
#     if max_idx < num_idx :
#       result, max_idx = num, num_idx
  
#   return result



# a = int(input())
# q = 1
# w = 2
# while a-2:
#     q, w = w , q + w
#     a -= 1
# print(w)   



# N, K = map(int,input().split(' '))
# use = list(map(int,input().split(' ')))
# code = []
# answer = 0

# for this in range(K):
#     if use[this] in code :  # 코드에 이미 꽂혀져있음
#         continue

#     if len(code) < N :  # 코드 자리 남음
#         code.append(use[this])
#         continue

#     priority = []
#     for c in code:  # 꽂혀져 있는 코드들
#         if c in use[this:]: # 다음에 또 이용해야한다면
#             priority.append(use[this:].index(c))
#         else:
#             priority.append(101)
#     target = priority.index(max(priority))
#     code.remove(code[target])
#     code.append(use[this])
#     answer += 1

# print(answer)

# import sys


# def dfs(start, now, value, cnt):
#     global ans
#     if cnt == N:
#         if a[now][start]:
#             value += a[now][start]
#             if ans > value:
#                 ans = value
#         return

#     if value > ans:
#         return

#     for i in range(N):
#         if not visited[i] and a[now][i]:
#             visited[i] = 1
#             dfs(start, i, value + a[now][i], cnt + 1)
#             visited[i] = 0


# N = int(input())
# a = [list(map(int, input().split()))for _ in range(N)]
# ans = sys.maxsize
# visited = [0] * N
# for i in range(N):
#     visited[i] = 1
#     dfs(i, i, 0, 1)
#     visited[i] = 0
# print(ans)

# visited = [0,1,1,1,0,24,567,0]
# print(visited.count(1))

a  = bin(-7)
b = [0,1,1,1,0,0]

print(a)
print(a)
