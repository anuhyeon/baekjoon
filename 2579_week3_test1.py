import sys
n = int(sys.stdin.readline().rstrip())
num = [0]*(n+1)

for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))
val = [0]*(n+1)
val[1] = num[1]
val[2] = num[1]+num[2]
val[3] = max(num[1]+num[2], num[1]+num[3])
i=4
while i<=n:
    val[i] = max(val[i-3]+num[i]+num[i-1],val[i-2]+num[i])
    i += 1


print(max(val))




