# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    s = input()
    if(re.findall(r'\<[a-zA-Z]{1}[a-zA-Z0-9\-\.\_]{1,}\@[a-zA-Z]{1,}\.[a-zA-Z]{1,3}\>',s)!=[]):
        print(s)
