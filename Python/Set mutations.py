# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
n = int(input())
for i in range(n):
    x = input().split()
    b = set(map(int,input().split()))
    if x[0] == 'intersection_update':
        a&=b
    elif x[0] == 'update':
        a|=b
    elif x[0] == 'symmetric_difference_update':
        a^=b
    elif x[0] == 'difference_update':
        a-=b
print(sum(a))
