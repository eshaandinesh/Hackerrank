def wrap(string, max_width):
    s = ''
    for i in range((len(string)//max_width)):
        s = s + (string[0:max_width]+"\n")
        string = string[max_width:]
    s = s+string[0:max_width]
    return s

