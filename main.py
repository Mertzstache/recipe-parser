#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run this"""


import sys
from parseallrecipes import ARParser
from recipe import Recipe


def main():


    """main function - default google.com"""
    url = "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"

    if len(sys.argv) > 2:
        url = sys.argv[2]

    parser = ARParser(url)
    recipe = parser.parse_recipe()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'double':
            recipe.multiply_portion(2)
        elif sys.argv[1] == 'healthy':
            recipe.make_healthy()
        elif sys.argv[1] == 'spicy':
            recipe.make_in_style("spicy")
        elif sys.argv[1] == 'hawaiian':
            recipe.make_in_style("hawaiian")
        elif sys.argv[1] == 'vegetarian':
            recipe.make_vegetarian()
        elif sys.argv[1] == 'nonvegetarian':
            recipe.make_nonvegetarian()

    print(recipe)


if __name__ == "__main__":
    main()
