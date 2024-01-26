# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
c = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
v = 'aeiouAEIOU'
x = re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(c,v,c),s)
if x!=[]:
    for i in range(len(x)):
        print(x[i])
else:
    print(-1)   
