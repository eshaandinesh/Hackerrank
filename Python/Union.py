# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int,input().split()))
b = int(input())
s2 = set(map(int,input().split()))
print(len(s.union(s2)))
