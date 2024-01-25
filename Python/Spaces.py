def print_formatted(number):
    # your code goes here
    x = len(bin(number))-2
    o = 0
    h = 0
    b = 0
    for i in range(1,number+1):
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        i = str(i)
        print(i.rjust(x),o.rjust(x),h.rjust(x),b.rjust(x))

