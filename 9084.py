import sys
t = int(sys.stdin.readline().rstrip())

def knap_sack(n,money,coins):
    dp = [[0]*(money+1) for _ in range(n+1)] #2차원배열 생성 + 0 패딩 
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,money+1):
            if coins[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    return dp[n][money]
answer = [] 

for _ in range(t):
    
    n = int(sys.stdin.readline().rstrip()) # 코인의 개수
    coins = list(map(int,sys.stdin.readline().split()))
    coins = [0] + coins  
    money = int(sys.stdin.readline().rstrip())
    print(knap_sack(n,money,coins))
    




