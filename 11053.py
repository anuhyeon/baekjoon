import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().split()))
val = [1]
for i in range(1,n):
    ls = [0]
    for j in range(len(A[:i])):
        if A[i] > A[j]:
            ls.append(val[j])
    val.append(max(ls)+1)
print(val)
                
            
# import sys
# def input():
#     return sys.stdin.readline().rstrip()


# N = int(input())
# arr = list(map(int, input().split()))
# # print(arr) [10, 20, 10, 30, 20, 50]
# dp = [1] * N

# for i in range(1, N):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
            

# print(max(dp))

#10 50 20 30 20 40 60 70 80 90
