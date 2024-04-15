import sys
n, m = map(int,sys.stdin.readline().split())

graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)] 
# print(graph)
# print()
# print(graph[0][0])


def dfs(G,x,y,visited):
    visited[x][y] = 1
    if G[x][y] == '|':
        if x+1<len(G) and G[x+1][y] == '|' and visited[x+1][y] == 0:
            dfs(G,x+1,y,visited)
        
    elif G[x][y] == '-':
        if y+1<len(G[0]) and G[x][y+1] == '-' and visited[x][y+1] == 0:
            dfs(G,x,y+1,visited)
        

def solution(G,visited):
    global n,m
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                dfs(G,i,j,visited)
                cnt += 1
    return cnt

print(solution(graph,visited))
