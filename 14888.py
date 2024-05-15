import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))

maximum = int(-1e9)
minimum = int(1e9)

def dfs(ans,index,add,sub,mul,div):
    global maximum, minimum,n
    if index == n-1: 
        if ans < minimum:
            minimum = ans
        if ans > maximum:
            maximum = ans
        return 
    if add > 0:
        dfs(ans+arr[index+1],index+1,add-1,sub,mul,div)
    if sub > 0:
        dfs(ans-arr[index+1],index+1,add,sub-1,mul,div)
    if mul > 0:
        dfs(ans*arr[index+1],index+1,add,sub,mul-1,div)
    if div > 0:
        dfs(int(ans/arr[index+1]),index+1,add,sub,mul,div-1)

dfs(arr[0],0,cal[0],cal[1],cal[2],cal[3])
print(maximum)
print(minimum)