# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())
for i in range(t):
    s = ''.join(sorted(input()))
    if(re.match(r'[a-zA-Z0-9]{10}',s) and re.findall(r'(.)\1', s)==[] and re.findall(r'[A-Z]{2,}',s)!=[] and re.findall(r'[0-9]{3,}',s)!=[]):
        print('Valid')
    else:
        print('Invalid')
