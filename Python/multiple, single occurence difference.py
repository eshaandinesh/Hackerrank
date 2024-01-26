# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
lis = list(map(int, input().split()))
#s = set(lis)
single = set()
multiple = set()
for i in lis:
    if i in single:
        multiple.add(i)
    else:
        single.add(i)
print(single.difference(multiple).pop())
