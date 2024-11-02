# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start".ljust(5), ":", tag)
        for n, v in attrs:
            print(f"-> {n} > {v}")
    def handle_endtag(self, tag):
        print("End".ljust(5), ":", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(5), ":", tag)
        for n, v in attrs:
            print(f"-> {n} > {v}")
t = ''.join(input() for _ in range(int(input())))
parser = MyHTMLParser()
parser.feed(t)
