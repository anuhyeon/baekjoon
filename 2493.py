import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack = []
for i in range(n):
    height = int(input().rstrip())
    stack.append(height)
    

print(stack)