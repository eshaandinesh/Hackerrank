# Enter your code here. Read input from STDIN. Print output to STDOUT
x,k = input().split()
x = float(x)
k = float(k)
p = input()  #.replace('x','1')
#print(p)
if eval(p) == k:
    print('True')
else:
    print('False')
