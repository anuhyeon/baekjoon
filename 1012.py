import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    graph = [[]*n for _ in range()]
