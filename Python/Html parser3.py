# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for i in attrs:
            print('->',i[0],'>',i[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n = int(input())
for i in range(n):
    parser.feed(input())
