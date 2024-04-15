import sys
n,k = map(int,sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

cnt = 0

while coins:
    coin = coins.pop()
    cnt += k // coin
    k = k % coin

print(cnt)
    
