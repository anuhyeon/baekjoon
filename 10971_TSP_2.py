import sys
n = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [0]*n
min = 1e9
ls = []
def dfs(start,cost,root):
    global n,min
    
    if cost > min:
        return
    
    if visited.count(1) == n:
        if graph[start][root]:
            cost += graph[start][root]
            # ls.append(cost)
            if cost < min:
                min = cost
        return
    
    for i in range(n):
        if visited[i] == 0 and graph[start][i] != 0:
            visited[i] = 1
            #cost += graph[start][i]
            dfs(i,cost + graph[start][i],root)
            # cost -= graph[start][i]
            visited[i] = 0
        
      
for i in range(n):
    visited[i] = 1
    dfs(i,0,i)
    visited = [0]*n

# print(ls)
# print(len(ls))
print(min)

# 4
# 0 10 15 1
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0