# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n = int(input())
    if n==1:
        print('Not prime')
    elif n%2==0 and n>2:
        print('Not prime')
    else:
        for j in range(3,int(n**(1/2)+1),2):
            if(n%j==0):
                print('Not prime')
                break   
        else: 
            print('Prime')
