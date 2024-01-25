# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

x,n = input().split()
x = list(x)
x.sort()
s = ''.join(str(i) for i in x)
n = int(n)
l = list(permutations(s,n))
for i in l:
    print("".join(j for j in i ))
