#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""recipe class"""

from urllib import request
from bs4 import BeautifulSoup

class Recipe():
    """class to keep track of recipe info"""

    def __init__(self, url):

        response = request.urlopen(url)
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')


        self.ingredients = []
        self.directions = []

        ingred = soup.findAll("span", {"class": "recipe-ingred_txt added"})
        direct = soup.findAll("span", {"class": "recipe-directions__list--item"})


        for span in ingred:
            self.ingredients.append(str(span.string))

        for span in direct:
            if span.string != None:
                self.directions.append(str(span.string))

    def __str__(self):
        """simple output function"""
        return_me = "\nINGREDIENTS\n\n"
        for line in self.ingredients:
            return_me += line + "\n\n"
        return_me += "DIRECTIONS\n\n"
        for line in self.directions:
            return_me += line + "\n\n"
        return return_me

    def add_direction(self, direction_text):
        """use this fuciton when you want to add a direciton to the END of a recipe"""
        self.directions.append(direction_text)

    def substitue_ingredient(self, previous, new):
        """this is a simple idea of replacing one WHOLE INGREDIENT DIRECTION with a new one"""
        self.ingredients.remove(previous)
        self.ingredients.append(new)
        #look through all instances in directions and replace as well
