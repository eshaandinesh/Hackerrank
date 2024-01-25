# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,n = input().split()
n = int(n)
s = list(s)
s.sort()
s = "".join(i for i in s)
l = list(combinations_with_replacement(s,n))
for i in l:
    print("".join(x for x in i))
