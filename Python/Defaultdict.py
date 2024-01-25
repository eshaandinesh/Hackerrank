# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = input().split()
d = defaultdict(list)
for i in range(int(n)):
    x = input()
    d[x].append(i+1)

for i in range(int(m)):
    x = input()
    if len(d[x])>0:
        print(*d[x]) 
    else:
        print('-1')
