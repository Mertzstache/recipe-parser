#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run this"""


import sys
from parseallrecipes import ARParser
from recipe import Recipe


def main():


    """main function - default google.com"""
    url = "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"
    def transform(x):
	    {
	        'double': recipe.multiply_portion(2),
            'vegetarian': recipe.make_vegetarian(),
            'healthy': recipe.make_healthy(),
            'spicy': recipe.make_in_style("spicy"),
            'hawaiian': recipe.make_in_style("hawaiian")
	    }[x]

    # url = "https://www.allrecipes.com/recipe/256753/irish-soda-bread-muffins/?internalSource=staff%20pick&referringId=197&referringContentType=recipe%20hub"
    if len(sys.argv) > 2:
        url = sys.argv[2]

    parser = ARParser(url)
    recipe = parser.parse_recipe()


    recipe.make_in_style("hawaiian")
    # if len(sys.argv) > 1:
    # 	transform(sys.argv[1])

    print(recipe)


if __name__ == "__main__":
    main()
