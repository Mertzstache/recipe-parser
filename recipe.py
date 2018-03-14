#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""recipe class"""


class Recipe():
    """class to keep track of recipe info"""

    def __init__(self, ingredients, instructions, tools, parsed_instructions):

        self.ingredients = ingredients
        self.instructions = instructions
        self.tools = tools
        self.parsed_instructions = parsed_instructions

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
        for instruction in range(len(self.parsed_instructions)):
            return_me += '\n\n' + 'instruction ' + str(instruction) + ' ' + str(self.parsed_instructions[instruction])
        return return_me

    def substitue_ingredient(self, previous, new):
        """this is a simple idea of replacing one WHOLE INGREDIENT DIRECTION with a new one"""
        # self.ingredients.remove(previous)
        # self.ingredients.append(new)
        #look through all instances in directions and replace as well

        pass

    def multiply_portion(self, multiplier):
        """takes in integer multiplier"""
        for i,ing in enumerate(self.ingredients):
            numbers = ing[0].split(' ')
            output_arr = []
            for n in numbers:
                if "/" in n:
                    output_arr.append(n.replace(n[0], str(int(n[0])*multiplier)))
                else:
                    output_arr.append(str(int(n)*multiplier))
            self.ingredients[i][0] = ' '.join(output_arr)


