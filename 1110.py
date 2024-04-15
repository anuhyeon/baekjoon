#26 = 08  1
#68 = 14  2
#84 = 12  3
#42 = 06  4
#26

import sys
input = sys.stdin.readline
n = int(input().rstrip())
def cycle(n):
    cnt = 0
    d = n  
    while True:
        sum = n//10 + n%10 #8
        n = (n%10)*10 + sum%10
        cnt += 1
        if d == n:
            return cnt
        
    
print(cycle(n))
