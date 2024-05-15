import sys
str = sys.stdin.readline().rstrip()
#arr = [s for s in str]
#print(arr)

def correct(str):
    cnt = 0 # 왼쪽 괄호의 갯수
    for i in str:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: # ')'인데 앞쪽에 왼쪽 괄호 친구가 없는 경우
                return False
            cnt -= 1
    return True
            

def balanced(str): # 균형잡힌 괄호 문자열의 인덱스 반환
    cnt = 0
    for i in range(len(str)):
        if str[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


def solution(p):
    if correct(p): 
        return str 

    answer = ''
    idx = balanced(p)
    if correct(p[:idx+1]):
        return p[:idx+1] + solution(p[idx+1:])
    else:
        answer += '('
        for i in p[1:idx]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        
        answer += ')'
        answer += p[idx+1:]
        return answer

print(solution(str))
    
# if correct(str): 
#     print(str)      
# else:
#     print(solution(str))