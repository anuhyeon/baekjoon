import sys
# def hanoi_step(n, source, target, auxiliary):
#     if n == 1:
#         return 1
#     count = 0
#     count += hanoi_step(n-1, source, auxiliary, target)
#     count += 1
#     count += hanoi_step(n-1, auxiliary, target, source)
#     return countcnt

cnt = 0
def hanoi(n, first, third, second):
    global cnt
    if n > 20:
        return
    
    if n == 1:
        print(first,third)
        cnt += 1
        return
    
    hanoi(n-1, first, second, third)
    hanoi(1, first, third, second)
    hanoi(n-1, second, third, first)

n = int(sys.stdin.readline().rstrip())

hanoi(n, 1, 3, 2)
print(cnt)


# def f(n):
#     if n==1:
#         return
#     else:
#        return(n의 변화) 


