import sys
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    input_str = sys.stdin.readline().rstrip()
    list = input_str.split()
    n = int(list[0])
    for k in list[1]:
        print(n*k,end="")
    print("")
        

