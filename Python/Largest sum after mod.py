# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k,m = input().split()
k = int(k)
m = int(m)
l = []
fin = []
for i in range(k):
    num = list(map(int,input().split()[1:]))
    num.sort(reverse = True)
    l.append(num)
for t in product(*l):
    s = 0
    for j in t:
        s += j**2
    fin.append(s%m)
print(max(fin))    
