import sys
import copy
n,k = map(int,sys.stdin.readline().split())
ls = list(map(int,sys.stdin.readline().split()))
hole = []
# print(hole)
# print(ls)
cnt = 0
for i in range(k):
    if ls[i] in hole:
        continue
    if len(hole) < n:
        hole.append(ls[i])
        continue
    else:
        idx = [] #idx 넣을 위치
        for s in hole:  
            if s in ls[i:]: 
                idx.append(ls[i:].index(s))
            else:
                idx.append(101)
    a = idx.index(max(idx))
    hole.remove(hole[a])
    hole.append(ls[i])
    cnt += 1     

print(cnt)


# 3 100
# 56 71 70 25 52 77 76 8 68 71 51 65 13 23 7 16 19 54 95 18 86 74 29 76 61 93 44 96 32 72 64 19 50 49 22 14 7 64 24 83 6 3 2 76 99 7 76 100 60 60 6 50 90 49 27 51 37 61 16 84 89 51 73 28 90 77 73 39 78 96 78 13 92 54 70 69 62 78 7 75 30 67 97 98 19 86 90 90 2 39 41 58 57 84 19 8 52 39 26 7