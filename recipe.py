#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""recipe class"""


class Recipe():
    """class to keep track of recipe info"""

    def __init__(self, ingredients, instructions, tools):

        self.ingredients = ingredients
        self.instructions = instructions
        self.tools = tools

        

    def __str__(self):
        """simple output function"""
        return_me = "\nINGREDIENTS\n\n"

        for item in self.ingredients:
            return_me += ' '.join(map(str, item)) + "\n"

        return_me += "\n\n"

        # return_me += "DIRECTIONS\n\n"
        for item in self.instructions:
            return_me += item + "\n\n"

        return_me += 'TOOLS USED: ' + ', '.join(self.tools)
        return return_me


    def substitue_ingredient(self, previous, new):
        """this is a simple idea of replacing one WHOLE INGREDIENT DIRECTION with a new one"""
        # self.ingredients.remove(previous)
        # self.ingredients.append(new)
        #look through all instances in directions and replace as well

        pass
