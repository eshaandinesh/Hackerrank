# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
x = set(map(int,input().split()))
b = input()
y = set(map(int,input().split()))
print(len(x.difference(y)))
