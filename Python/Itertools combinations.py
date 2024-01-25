# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,n = input().split()
s = list(s)
s.sort()
#for i in s: print (i)
s = "".join(str(i) for i in s)
n = int(n)
for x in range(1,n+1):
    c = list(combinations(s,x))
    for i in c:
        print("".join(str(j) for j in i))
