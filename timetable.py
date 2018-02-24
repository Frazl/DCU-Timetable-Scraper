#!/usr/bin/env python

from lxml import html
import requests
import json
import sys
import string

def fout(json):
    print("Please give a filename")
    s = str(input() + ".json")
    s = open(s, "w+")
    disallowed = "$#[]"
    for x in disallowed:
        json = json.replace(x, "")
    s.write(json)
    s.close()

def skinsscraper(tree):
    collection = {}
    name = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[4]')
    print(name)
    #fout(json.dumps(collection, sort_keys=True, indent=4, separators=(',', ': ')))
    
def main():
    page = requests.get("https://www101.dcu.ie/timetables/feed.php?prog=CA&per=1&week1=20&week2=31&hour=1-20&template=student", verify=False)
    x = page.content
    x = str(x)
    x = x.split("<!-- START ROW OUTPUT -->")
    x = x[1].split("<!-- END ROW OUTPUT -->")
    x = x[0].split("<td")
    print(x)
    tree = html.fromstring(page.content)
    skinsscraper(tree)
if __name__ == '__main__':
    main()