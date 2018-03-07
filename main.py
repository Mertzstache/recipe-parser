#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run this"""


import sys
from parseallrecipes import ARParser
from recipe import Recipe


def main():
    
    """main function - default google.com"""
    
    url = "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"

    if len(sys.argv) > 1:
        url = sys.argv[1]

    parser = ARParser(url)
    recipe = parser.parse_recipe()

    print(recipe)


if __name__ == "__main__":
    main()
