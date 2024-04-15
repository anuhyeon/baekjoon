import sys

string = sys.stdin.readline().rstrip()
ls = string.split("-")
toal = 0 
ls2 = []
for s in ls:
    plus_list =  list(map(int,s.split("+")))
    total = sum(plus_list)
    ls2.append(total)
for i in range(1,len(ls2)):
    ls2[0] -= ls2[i]
    
print(ls2[0])
    