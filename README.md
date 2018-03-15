# recipe-parser
A recipe parser that allows for different substitutions

We use python3 in this project. To run it with a default recipe ([World's Best Lasagna](https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/)), simply run:

`python3 main.py`

There are two optional arguments: transformation and recipe, which can be used as follows:

`python3 main.py <transformation> <allrecipes url>`

If you wish to provide a recipe but not a transformation, just run:

`python3 main.py normal <allrecipes url>`

Available transformations:
`double` (double the recipe quantity), `vegetarian`, `nonvegetarian`, `healthy`, `unhealthy`, `spicy`, `hawaiian`
