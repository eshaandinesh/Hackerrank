# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print ('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print (">>> Data\n", data,sep = '')

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n = int(input())
x = ''
for i in range(n):
    x = input()+'\n'
    parser.feed(x)
