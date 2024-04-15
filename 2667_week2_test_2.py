import sys
import heapq
from collections import deque
n = int(sys.stdin.readline().rstrip())

graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
nwes = [(1,0),(-1,0),(0,-1),(0,1)]
visited = [[0]*n for _ in range(n)]
cnt = 0
sum = 0
list = []

def dfs_recurs(G,i,j,visited):
    visited[i][j] = 1
    global sum 
    sum += 1
    for di,dj in nwes:
        if  0 <= i+di < len(G) and 0 <= j+dj < len(G[0]) and G[i+di][j+dj] == 1 and visited[i+di][j+dj] == 0:
            dfs_recurs(G,i+di,j+dj,visited)
    return True

#def dfs_stack(G):

def solution(G,visited):
    global cnt, sum
    for x in range(len(G)):
        for y in range(len(G[0])):
            if G[x][y] != 0 and visited[x][y] == 0:
                dfs_recurs(G,x,y,visited)
                cnt += 1 
                list.append(sum)
                sum=0
                

    return cnt

print(solution(graph,visited))
list.sort()
for i in range(len(list)):
    print(list[i])






