import sys
from collections import deque
m,n,h = map(int,sys.stdin.readline().split())
cnt = 0
tmtbox = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)]for _ in range(h)]
#tmtbox[h][n][m]
q = deque()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if tmtbox[z][i][j] == 1:
                q.append((z,i,j))
            elif tmtbox[z][i][j] == 0:
                cnt += 1
                
nwes = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]


def bfs(G):
    global cnt
    answer = 0
    max = 0
    while q:
        h,n,m  = q.popleft()
        for dh,dn,dm in nwes:
            if 0 <= h+dh < len(G) and 0<= n+dn < len(G[0]) and 0 <= m+dm < len(G[0][0]) and G[h+dh][n+dn][m+dm] == 0:
                G[h+dh][n+dn][m+dm] = G[h][n][m] + 1  
                if  G[h+dh][n+dn][m+dm] > max:
                    max = G[h+dh][n+dn][m+dm]
                q.append((h+dh,n+dn,m+dm))
                cnt -= 1
    
    if cnt != 0:
        return -1
    
    return max - 1         
        
       
if cnt == 0:
    print(0)
else:
    print(bfs(tmtbox))

# bfs(tmtbox)
# print(tmtbox)


#[
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],  --> tmtbox[h=0][n=1] 
#  [0, 0, 0, 0, 0]],
# [[0, 0, 0, 0, 0],  --> tmtbox[h=1][n=0]
#  [0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0]]  
#                   ]

# [[[5, 4, 3, 4, 5],
#   [4, 3, 2, 3, 4],
#   [5, 4, 3, 4, 5]],
#  [[4, 3, 2, 3, 4],
#   [3, 2, 1, 2, 3],
#   [4, 3, 2, 3, 4]]]