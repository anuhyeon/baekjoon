import sys
def quarter(x,y,n,arr): # x,y 좌표
    global res
    color = arr[x][y] # 첫번째 색을 가져옴
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                print("(",end="")
                quarter(x,y,n//2,arr)
                quarter(x,y+n//2,n//2,arr)
                quarter(x+n//2,y,n//2,arr)
                quarter(x+n//2,y+n//2,n//2,arr)
                print(")",end="")
                return 

    print(color,end="")

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)] 
    quarter(0,0,n,arr)
    print()