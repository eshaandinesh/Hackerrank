# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
#l =re.findall(r'([a-zA-Z0-9])\1',s)
#print(l[0])
m = re.search(r'([a-zA-Z0-9])\1', s)
print(m.group(1) if m else -1)
