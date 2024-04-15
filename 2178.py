import sys
from collections import deque

def BFS(G):
    visited = [[0]*len(G[0]) for _ in range(len(G))]
    visited[0][0] = 1
    queue = deque([(0,0)])
    nsew = [(1,0),(0,1),(-1,0),(0,-1)]
    before_x,before_y = 0,0
    
    while queue:
        now = queue.popleft() #pop을 방문했다라고 생각
        x,y = now
        #visited[x][y] = visited[before_x][before_y] + 1
        for next in nsew:
            dx,dy = next
            if 0 <= (x+dx) <= (len(G)-1) and 0 <= (y+dy) <= (len(G[0])-1) and visited[x+dx][y+dy] == 0 and G[x+dx][y+dy] != 0:
                queue.append((x+dx, y+dy))
                visited[x+dx][y+dy] = visited[x][y] + 1  # 아직 방문하지 않았지만 방문할 예정인 경우 그냥 visited 체크
                
        #before_x,before_y = x,y    
    
    return visited[len(G)-1][len(G[0])-1]


if __name__ =="__main__":
    n,m = map(int,sys.stdin.readline().split())
    graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
    
    print(BFS(graph))
    