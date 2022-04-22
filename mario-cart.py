# See https://stackoverflow.com/questions/51657000/how-to-convert-an-html-table-into-a-python-dictionary

import csv
import requests
from html.parser import HTMLParser


class MkwrsParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.table = [[]]
        self.data = None
        self.capture = False

    def handle_endtag(self, tag):
        if self.capture:
            if tag == 'th' or tag == 'td':
                self.table[-1].append(self.data)
            if tag == 'tr':
                self.table.append([])

    def handle_data(self, data):
        self.data = data.strip()
        if 'Recent World Records' == self.data:
            self.capture = True


response = requests.get('https://mkwrs.com')

parser = MkwrsParser()
parser.feed(response.text)

with open('output/mario-cart.csv', 'w') as csvfile:
    csv.writer(csvfile).writerows(parser.table)
