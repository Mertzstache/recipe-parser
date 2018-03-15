#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""recipe class"""

from constants import *
import random

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
        for i,instruction in enumerate(self.parsed_instructions[:-1]):
            return_me += '\n\n' + 'Step ' + str(i + 1) + ':'
            for k in instruction.keys():
                return_me += "\n\t" + k + ": " + str(instruction[k])
        return return_me



    def make_healthy(self):
        # self._substitute_ingredient(HEALTH_INGRED_SUB)

        sub_map = []

        for idx, ingred in enumerate(self.ingredients):
            new_ingred = self._sub_key_pair(HEALTH_INGRED_SUB, ingred[2])

            if new_ingred:
                sub_map.append((ingred[2], new_ingred))
                self.ingredients[idx][2] = new_ingred

            else:
                new_ingred = self._substitute_ingredient_class(ingred[2], MEAT, VEG_MEAT)

                if new_ingred:
                    sub_map.append((ingred[2], new_ingred))
                    self.ingredients[idx][2] = new_ingred

            self.ingredients[idx][2] = "free-range organic non-gmo gluten-free " + self.ingredients[idx][2]
        self.instructions = self._substitute_direction_class(self.instructions, MEAT, VEG_MEAT)




    def make_vegetarian(self):

        sub_map = []

        for idx, ingred in enumerate(self.ingredients):
           
            new_ingred = self._substitute_ingredient_class(ingred[2], MEAT, VEG_MEAT)

            if new_ingred:
                sub_map.append((ingred[2], new_ingred))
                self.ingredients[idx][2] = new_ingred
        self.instructions = self._substitute_direction_class(self.instructions, MEAT, VEG_MEAT)





    def make_in_style(self):
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




    # def _substitute_ingredient(self, pair_dict):
    #     """this is a simple idea of replacing one WHOLE INGREDIENT DIRECTION with a new one"""
    #     # self.ingredients.remove(previous)
    #     # self.ingredients.append(new)
    #     #look through all instances in directions and replace as well

    #     for idx, ingred in enumerate(self.ingredients):
    #         self.ingredients[idx][2] = self._sub_key_pair(pair_dict, ingred[2])


    def _sub_key_pair(self, pair_dict, item):
        if item in pair_dict.keys():
            return pair_dict[item]
        
        return None


    def _substitute_ingredient_class(self, ingred, from_class, to_class):
        
        if ingred in from_class:
            return random.choice(to_class)

        return None

    def _substitute_direction_class(self, direction, from_class, to_class):
        new_direction = direction[:]
        for i in from_class:
            print(i)
            for j, direction in enumerate(new_direction):
                if i in direction:
                    print("hi we got here")
                    new_direction[j] = new_direction[j].replace(i, random.choice(to_class))
        return new_direction

    def _transform_ingred(self, ttype):

        for ingred in self.ingredients:
            print(ingred)
