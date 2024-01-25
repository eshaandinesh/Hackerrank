def count_substring(string, sub_string):
    x = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            x += 1
            
    return x

