import sys
import heapq
n = int(sys.stdin.readline().rstrip())
time = []
for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(time,(end,start))

idx = 0
conference = []
heapq.heappush(conference,(heapq.heappop(time)))
while time:
    now_end,now_start = conference[idx] 
    #import pdb; pdb.set_trace()
    next_end,next_start = heapq.heappop(time)
    if now_end <= next_start:
        heapq.heappush(conference,(next_end,next_start))
        idx += 1

print(len(conference))
#print(conference)


# 6
# 0 0
# 0 1
# 1 2
# 1 3
# 2 3
# 3 3

# 0,0  1,2  2,3  3,3
#4