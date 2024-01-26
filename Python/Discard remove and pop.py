# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    x = input().split()
    try:
        if x[0]=='pop':
            s.discard(min(s))
        elif x[0]=='remove':
            s.remove(int(x[1]))
        elif x[0]=='discard':
            s.discard(int(x[1])) 
        #else:
        #    s.discard(int(x[1]))
    except KeyError:
        continue 
print(sum(s))
