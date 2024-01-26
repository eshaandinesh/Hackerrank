

def get_attr_number(node):
    # your code goes here
    return sum(len(i.attrib) for i in node.iter())

