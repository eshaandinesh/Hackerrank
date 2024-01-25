# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools 
s = input()
for i,j in itertools.groupby(s):
    print((len(list(j)),int(i)),end = ' ')
