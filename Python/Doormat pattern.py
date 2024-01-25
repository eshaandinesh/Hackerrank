# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input().split()
n = int(x[0])
m = int(x[1])
p = '.|.'
s = 1
for i in range(n):
    if i == n//2:
        print('WELCOME'.center(m,'-'))
        s -= 2
        continue
    elif i <= n//2:
        print((p*s).center(m,'-'))
        s += 2
    elif i >= n//2:
        print((p*s).center(m,'-'))
        s -= 2
