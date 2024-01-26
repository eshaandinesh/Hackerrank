# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    l = deque(map(int,input().split()))
    
    for i in reversed(sorted(l)):
        if l[0] == i: l.popleft()
        elif l[-1] == i: l.pop()
        else:
            print('No')
            break
    else: print('Yes')
