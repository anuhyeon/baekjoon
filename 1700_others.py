import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

electronics = list(map(int,input().split()))

multitap = []
cnt = 0
for idx in range(len(electronics)):

    #이미 꽂혀 있으면 걍 넘어감.
    if electronics[idx] in multitap:
        continue

    #멀티탭이 아직 안채워졌으면, 배열에 삽입
    if len(multitap) < N:
        multitap.append(electronics[idx])

    #멀티탭이 다 채워짐
    else:
        tmplst = []
        #idx 뒤에서 부터 나올 전자기기가 있는지 확인
        for i in range(idx+1,len(electronics)):
            
            if len(tmplst) == N-1:
                    break

            if electronics[i] in multitap:
                tmplst.append(electronics[i])
                
        
            
    
        if tmplst:
            for n in multitap:
                if n not in tmplst:
                    #뒤에 나오지 않은 애 삭제
                    multitap.remove(n)
                    break
        else:
            #아무거나 삭제
            multitap.pop()

        #멀티탭에 새로운 값 채워넣기
        multitap.append(electronics[idx])
        cnt += 1

print(cnt)





