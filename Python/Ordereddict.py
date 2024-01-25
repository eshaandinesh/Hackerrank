# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dic = OrderedDict()
for i in range(n):
    x = input().split()
    key = ' '.join(x[0:len(x)-1])
    val = int(x[-1])
    if key in dic:
        dic[key]+= val
    else:
        dic[key] = val
for i in dic:
    print(i,dic[i])
