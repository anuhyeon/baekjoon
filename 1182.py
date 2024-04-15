import sys
from itertools import combinations
input = sys.stdin.readline
n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0

for i in range(1,n+1):
    for comb in combinations(arr,i):
        if sum(comb) == s:
            cnt += 1

print(cnt)
            