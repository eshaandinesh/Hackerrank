# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    s = input()
    if(re.findall(r'^[789][0-9]{9}$',s)!=[]):
        print('YES')
    else:
        print('NO')
