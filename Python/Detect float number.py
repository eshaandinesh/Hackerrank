# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for i in range(t):
    n = input()
    print(bool(re.fullmatch('^[-+]?[0-9]*[.][0-9]+',n)))
