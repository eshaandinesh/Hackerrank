# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p1 = r'^[456]\d{15}$|^[456]\d{3}-\d{4}-\d{4}-\d{4}$'
p2 = r'(\d-?)\1\1\1'
n = int(input())
for i in range(n):
    s = input()
    x = re.findall(p1,s)
    if x==[]:
        print('Invalid')
    else:
        for j in x:
            s2 = re.sub('-','',s)
            y = re.findall(p2,s2)
            if y != []:
                print('Invalid')
            else:
                print('Valid')        
