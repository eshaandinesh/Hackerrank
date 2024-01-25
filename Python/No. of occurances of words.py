# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dic = OrderedDict()
for i in range(n):
    x = input()
    if x in dic:
        dic[x]+=1
    else:
        dic[x] = 1
print(len(dic))
for i in dic:
    print(dic[i],end = ' ')
