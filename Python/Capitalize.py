

# Complete the solve function below.
def solve(s):
    x = []
    s = s.split(" ")
    print(s)
    for i in s:
        x.append(i.capitalize())
    return(' '.join(x))   

