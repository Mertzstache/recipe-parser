import util
import urllib
import constants
import re
from bs4 import BeautifulSoup

from recipe import Recipe


class ARParser():

	def __init__(self, url):

		response = urllib.request.urlopen(url)
		body = response.read()
		self.soup = BeautifulSoup(body, 'html.parser')



	def parse_recipe(self):
		return Recipe(self._get_ingredients(), self._get_instructions(), self._get_tools(), self._parse_instructions())




	def _process_ingredient_string(self, string):

		name = ''
		ind = 0
		quant = None
		extra_instructions = None
		descriptor = []

		match = re.match(r'[\d\/]+', string)
		if match:
			quant = match.group(0)
			ind = match.end()

		match = re.search(r'\(([^\)]+)\)', string)
		if match:
			descriptor.append(match.group(0))
			string = string.replace(' ' + match.group(0), '')

		keyword = util.string_has_keyword(string, constants.UNITS)

		for i in range(0, len(string)):
			if ',' in string[i]:
				extra_instructions = string[(i+1):]



		if not keyword:
			print("couldn't find a unit of measurement for", string)
			return (quant, string[ind:], string[ind:], None , extra_instructions)

		
		match = re.search(r"(" + re.escape(keyword) + r"s?)\s*", string)
		unit = match.group(1)

		end = len(string)
		if ',' in string:
			end = string.index(',')
		temp, name = string[match.end():end].split(' ')[:-1], string[match.end():end].split(' ')[-1]
		for d in temp:
			descriptor.append(d)

		#replaced with name string[match.end():]
		# print(string)
		return (quant, unit, name, descriptor, extra_instructions) # Nones are placeholders for descriptor, prep

	def _parse_instruction_sentence(self, sentence):
		properties = {}
		keyword = util.string_has_keyword(sentence, constants.TIME)
		if not keyword:
			print("no time specified", sentence)
			properties['time'] = 'no time specified'
		else:
			match = re.search(r"(?:(?!,).)*", sentence[sentence.index(keyword):])
			time = match.group(0)
			properties['time'] = str(time)
		return properties




	def _process_tools(self, instructions):
		paragraph = ' '.join(instructions)
		return util.string_has_keywords_multiple(paragraph, constants.TOOLS)

	def _parse_instructions(self):
		instructions_parsed = []
		for i in ' '.join(self._get_instructions()).split('.'):
			instructions_parsed.append(self._parse_instruction_sentence(i))
		return instructions_parsed

	def _get_ingredients(self):

		section = self.soup.find('ul', id='lst_ingredients_1').find_all("span", {"itemprop" : "ingredients"})
		section += self.soup.find('ul', id='lst_ingredients_2').find_all("span", {"itemprop" : "ingredients"})

		return [self._process_ingredient_string(ingred.text) for ingred in section]

	def _get_tools(self):
		return self._process_tools(self._get_instructions())

	def _get_instructions(self):
		section = self.soup.find('ol', {"class": "recipe-directions__list"}).find_all("span", {"class": "recipe-directions__list--item"})
		return [item.text for item in section]


	def _get_prep_time(self):
		return self.soup.find("time", {"itemprop": "prepTime"})["datetime"]


	def _get_cook_time(self):
		return self.soup.find("time", {"itemprop": "cookTime"})["datetime"]


	def _get_total_time(self):
		return self.soup.find("time", {"itemprop": "totalTime"})["datetime"]


	def _get_nutrition(self):
		return self.soup.find("section", {"class": "recipe-footnotes"}).find_all("span", itemprop=True)


