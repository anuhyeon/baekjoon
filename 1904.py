# n = 1 1          ->1
# n = 2 00 11      ->2 ->
# n = 3 00 1 / 1 00 / 11 1   ->3    -> 2+1
# n = 4 0011 / 1100 / 1111 / 0000 / 1 00 1 5개 만들 수 있음  -> 2^2 + 1
# n = 5 0011 1 / 1 0011 / 1 1100 / 1100 1 / 11111 / 1 0000 / 0000 1 / 1 1001 / 1001 1 / 00 1 00-> 2(2^2 +1) 
# n = 6 001100  1 00 1 00 1 /  11 1 00 1 / 1 00 11 1  ->2^3 +3

# n = 2 를 가지고 n=3,n=4를 만들 수 있음
import sys
n = int(sys.stdin.readline().rstrip())


ans_1 = 1
ans_2 = 2

if n == 1:
    print(ans_1)
else:  
    for _ in range(n-2):
        ans_1, ans_2 = ans_2, (ans_1+ans_2)%15746
        #ans_2 %= 15746

    print(ans_2)



# answer = [0]*(n)
# answer[0] = 1
# answer[1] = 2

# for i in range(1,n-1):
#     answer[i+1] = (answer[i]+answer[i-1])%15746
# print(answer[n-1])
# print(answer)









