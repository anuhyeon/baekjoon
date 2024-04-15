import sys
# hint
# 분할 정복법: 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복(Conquer)
# 면의 모든 칸이 같은 색이 될 때까지 색종이를 1/4로 계속 분할하는 문제.
#1. N//2로 반복해서 탐색해야한다. 반복해서 탐색하기에 재귀를 사용하면 된다는 것을 알 수 있다.
# 2. 반복 탐색 과정 중 N//2로 4면을 분할하는 과정을 거치므로 분할정복 알고리즘을 사용해야한다.
# 3. 먼저 탐색하려는 시작 색상을 정해주고, 주어진 영역에서 탐색하는 과정에서 색상과 일치하지 않는 지점이 생긴다면, 분할해서 탐색하도록 알고리즘을 구성해주자.
# 4. 탐색에 성공했다면, 그때 시작 색상에 따른 각각의 갯수를 세어주자
#
#
#
# while True:
#     n = int(sys.stdin.readline().rstrip())
#     if n == 2 or n == 4 or n == 8 or n == 16 or n == 32 or n == 64 or n == 128 :
#         break
# #print(n)
import sys
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 2차원 배열 선언

white = 0
blue = 0

def quarter(x,y,n): # x,y 좌표
    global white,blue,arr
    color = arr[x][y] # 첫번째 색을 가져옴
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                quarter(x,y,n//2)
                quarter(x,y+n//2,n//2)
                quarter(x+n//2,y,n//2)
                quarter(x+n//2,y+n//2,n//2)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1
        


quarter(0,0,n)   
print(white)
print(blue) 
    

