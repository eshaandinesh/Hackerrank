# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
l = Counter(list(map(int,input().split())))
n = int(input())
s = 0
for i in range(n):
    x = list(map(int,input().split()))
    if(x[0] in l and l[x[0]] != 0):
        s+= x[1]
        l[x[0]] = l[x[0]] - 1
print (s)
