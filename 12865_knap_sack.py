import sys
n, k = map(int,sys.stdin.readline().split())
item = [(0,0)] # (Weight,Value)
for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    item.append((w,v))

#item = [(0, 0), (6, 13), (4, 8), (3, 6), (5, 12)] # 아이템은 딱 한번만 사용가능 쪼개기도 불가능
# Weight = item[i][0] 
# Value = item[i][1]
dp = [[0]*(k+1) for _ in range(n+1)]  # 0으로 패딩, i는 아이템의 인덱스, j는 무게들
#dp[i][j]--> jkg을 담을 수 있는 가방에 i번 이하의 아이템들로 최대의 가치를 저장 
for i in range(1,n+1):
    for j in range(1,k+1):
        if item[i][0] > j: # i번 아이템을 못 넣는 경우: i번 아이템의 무게가 jkg(가방의 허용 무게)를 넘어선다면 이전 인덱스(i-1)번 아이템을 jkg가방에 담을 수 있는 최대의 가치값을 넣어준다.
            dp[i][j] = dp[i-1][j] # i번 아이템을 사용하지 않고 만들 수 있는 최대가치
        else: 
            # i번 아이템을 넣을 수 있는 경우: 무작정 넣는다고 최대의 가치를 나타내는 것은 아니므로 i번 아이템을 가방에 넣었을 경우 와 i번 아이템을 가방에 넣지 않을 경우 두가지를 따져 봐야한다.
            # i번 아이템을 넣는 경우 : i번 아이템의 가치 + (jkg - i번item의 무게)에서의 최대가치 --> 여기서 (jkg - i번item의 무게)에서의 최대가치는 이전에 이미 i-1번 이하의 아이템들로 구성되어있을테니 dp[i-1][j-item[i][0]]이다.  --> i번 아이템을 사용하면서 만들 수 있는 최대가치
            # (jkg - i번item의 무게)에서의 최대가치 = dp[i-1][j-item[i][0]]
            # i번 아이템을 넣지 않는 경우 : 현재 jkg에서 이전에 i-1번 이하의 아이템들로 이루어진 최대가치 = dp[i-1][j]  --> i번 아이템을 사용하지 않고 만들 수 있는 최대가치
            # i번 아이템을 넣는 경우 vs i번 아이템을 넣는경우 --> i번 아이템의 가치 + (jkg - i번item의 무게)에서 이전에 i-1번 이하의 아이템들로 이루어진 최대가치 vs 현재 jkg에서 이전에 i-1번 이하의 아이템들로 이루어진 최대가치 
            # item[i][1] + dp[i-1][j-itme[i][0]] vs dp[i-1][j]
            dp[i][j] = max(item[i][1] + dp[i-1][j-item[i][0]],dp[i-1][j])

print(dp[n][k])

####추가 코드(백준이랑 상관 X)####
####백트래킹을 통한 역추적을 통한 어떤 배낭을 넣었는지 출력하는 코드####
selected_bag = []
def back_tracking(i,j): # 무게로 역추적
    global n,k, selected_bag,item,dp
    if i == 0 or j == 0: # 종료조건
        return
    if dp[i][j] == dp[i-1][j]: # i번 아이템을 넣지 않는 경우를 채택한 것이므로 i번 아이템은 넣지 않은 경우라고 보면됨
        back_tracking(i-1,j)
    else: # i번 아이템을 넣은 경우를 채택한 경우
        j = j-item[i][0] #현재 i번아이템의 무게를 빼서, j-i번 아이템 무게 상태로 감
        selected_bag.append(item[i]) # i번 아이템은 사용했으므로 넣어줌
        back_tracking(i-1,j) # 한칸위(i-1), j-(i번 아이템 무게) 상태로 가서 다시 역추적

back_tracking(n,k)
print(selected_bag)