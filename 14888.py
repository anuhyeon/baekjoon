import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip()))
add,sub,mul,div = map(int,sys.stdin.readline().split())

max = -1e9
min = 1e9


def DFS()