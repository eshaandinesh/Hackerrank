# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    x = input().split()
    if 'append' in x:
        d.append(x[1])
    elif 'appendleft' in x:
        d.appendleft(x[1])
    elif 'pop' in x:
        d.pop()
    elif 'popleft' in x:
        d.popleft()
for i in d: print(i, end = ' ')
