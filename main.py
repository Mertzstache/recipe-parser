#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Getting Frequency Dictionary"""

from html.parser import HTMLParser
from urllib import request
import sys
from bs4 import BeautifulSoup
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    """a class overriding HTML parser"""
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

def output(ingredients, directions):
    print("INGREDIENTS\n")
    for i in ingredients:
        print(i + "\n")
    print("DIRECTIONS\n")
    for d in directions:
        print(d + "\n")


def main():
    """main function - default google.com"""
    url = 'https://www.google.com'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    parser = MyHTMLParser()
    
    response = request.urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    # mydivs = soup.findAll('div')


    ingredients = []
    directions = []

    mySpansIng = soup.findAll("span", {"class": "recipe-ingred_txt added"})
    mySpansDir = soup.findAll("span", {"class": "recipe-directions__list--item"})


    for li in mySpansIng:
        ingredients.append(str(li.string))

    for span in mySpansDir:
        if span.string != None:
            directions.append(str(span.string))

    output(ingredients,directions)

    # print(soup.prettify)

    # print(soup.findall('recipe-directions__list--item'))
    # print(page_source)
    # parser.feed(page_source)

if __name__ == "__main__":
    main()
