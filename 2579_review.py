import sys 

def solve():
    n = int(sys.stdin.readline().rstrip())  # 계단 개수
    arr = [0]  # 계단 점수 리스트 초기화
    for _ in range(n):  # n개의 계단 점수 받기
        x = int(sys.stdin.readline().rstrip())
        arr.append(x) 
    g = [0, 0]  # g 리스트 초기화
    h = [0, arr[1]]  # h 리스트 초기화
    for i in range(2, n+1):  # 2번째 계단부터 n번째 계단까지 반복
        g.append(h[i-1] + arr[i])  # i-1번째 계단에서 i-2번째 계단을 밟지 않았을 때의 점수 + i번째 계단 점수
        h.append(max(h[i-2], g[i-2]) + arr[i])  # i-2번째 계단에서의 최대점수 + i번째 계단 점수

    print(max(g[n], h[n]))  # n번째 계단에서의 최대 점수 출력

solve()