import util
import urllib
import constants
import re
from bs4 import BeautifulSoup



class ARParser():

	def __init__(self, url):

		response = urllib.request.urlopen(url)
		body = response.read()
		self.soup = BeautifulSoup(body, 'html.parser')




	def _process_ingredient_string(self, string):

		ind = 0
		quant = None

		match = re.match(r'[\d\/]+', string)
		if match:
			quant = match.group(0)
			ind = match.end()

		keyword = util.string_has_keyword(string, constants.UNITS)

		if not keyword:
			print("couldn't find a unit of measurement for", string)
			return (quant, string[ind:], string[ind:])

		match = re.search(r"(" + re.escape(keyword) + r"s?)\s*", string)
		unit = match.group(1)

		return (quant, unit, string[match.end():])






	def _get_ingredients(self):

		ingredients = []

		section = self.soup.find('ul', id='lst_ingredients_1').find_all("span", {"itemprop" : "ingredients"})
		section += self.soup.find('ul', id='lst_ingredients_2').find_all("span", {"itemprop" : "ingredients"})

		return [self._process_ingredient_string(ingred.text) for ingred in section]




	def _get_instructions(self):
		section = self.soup.find('ol', id="recipe-directions__list").find_all("span", {"class": "recipe-directions__list--item"})
		return [item.text for item in section]


	def _get_prep_time(self):
		return self.soup.find("time", {"itemprop": "prepTime"})["datetime"]


	def _get_cook_time(self):
		return self.soup.find("time", {"itemprop": "cookTime"})["datetime"]


	def _get_total_time(self):
		return self.soup.find("time", {"itemprop": "totalTime"})["datetime"]


	def _get_nutrition(self):
		return self.soup.find("section", {"class": "recipe-footnotes"}).find_all("span", itemprop=True)






parser = ARParser("https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/")

ingreds = parser._get_ingredients()

for item in ingreds:
	print(item)