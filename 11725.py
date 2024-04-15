import sys
def DFS(G,start):
    dic = {}
    visited = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in G[v]:
                stack.append(w)
                
        else:
            for w in G[v]:
                dic[w] = v
    
    return visited,dic

def BFS(G,start):
    #visited = [start]
    queue = [start]
    dic = [0] * (len(G))

    while queue:
        v = queue.pop(0)
        for w in G[v]:
            if dic[w] == 0 and w != 1:
                #visited.append(w)
                queue.append(w)
                dic[w] = v
     
    for i in range(2,n+1):
        print(dic[i])           



if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    G = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int,sys.stdin.readline().split())
        G[u].append(v)               
        G[v].append(u)     
    #print(G)
    
    BFS(G,1)
    

                