#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run this"""

import sys
from recipe import Recipe


def main():
    """main function - default google.com"""
    url = 'https://www.google.com'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    recipe = Recipe(url)
    print(recipe)

if __name__ == "__main__":
    main()
