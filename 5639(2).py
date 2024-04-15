import sys
sys.setrecursionlimit(10**6)

num_list=[]
while True:
    try:
        num=int(sys.stdin.readline().rstrip())
        num_list.append(num)
    except:
        break
def postorder(left,right): # left : 리스트의 첫번째 인덱스  right : 리스트의 마지막 인덱스
    if left>right:
        return
    mid = right + 1
    for i in range(left+1,right+1):
        if num_list[i] > num_list[left]:
            mid = i
            break
    
    postorder(left+1,mid-1)
    postorder(mid,right)
    print(num_list[left])

postorder(0,len(num_list)-1)    
    