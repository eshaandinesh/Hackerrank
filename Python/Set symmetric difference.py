# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input().split()))
x = set(map(int,input().split()))
b = set(map(int,input().split()))
y = set(map(int,input().split()))
print(len(x.symmetric_difference(y)))
