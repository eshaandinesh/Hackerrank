# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    x = re.findall(r'#[0-9A-Fa-f]{6}(?=[;,\)])|#[0-9A-Fa-f]{3}(?=[;,\)])',input())
#    print(x[i] for i in range(len(x)) if x!=[])
    if(x!=[]):
        for i in range(len(x)):
            print(x[i])
