# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())
for i in range(t):
    a = input()
    try:
       re.compile(a)
       print('True')
    except re.error:
        print("False") 
