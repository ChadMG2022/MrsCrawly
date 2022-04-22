# See https://stackoverflow.com/questions/51657000/how-to-convert-an-html-table-into-a-python-dictionary

import requests
from html.parser import HTMLParser

class MkwrsParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

    def handle_endtag(self, tag):
        self.tags.pop()

    def handle_data(self, data):
        if data and data.strip():
            print(self.tags)
            print(data)
        # if data == 'Recent World Records':
        #     exit(0)


response = requests.get('https://mkwrs.com')
# print(response.text)

parser = MkwrsParser()
parser.feed(response.text)
print(parser.tags)
