import sys

str_1 = sys.stdin.readline().rstrip()  # --> i
str_2 = sys.stdin.readline().rstrip()  # --> j

n = len(str_1)   # --> i
m = len(str_2)  # --> j

lcs = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if str_1[i-1] == str_2[j-1]: #ㅜ 문자가 서로 같을 경우
            lcs[i][j] = lcs[i-1][j-1] + 1
        else: # 문자가 서로 다를 경우
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

print(lcs[n][m])

