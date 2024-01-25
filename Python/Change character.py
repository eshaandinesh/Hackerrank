def mutate_string(string, position, character):
    s = string[0:position]+character+string[position+1:]
    return s

