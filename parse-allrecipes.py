import urllib
from bs4 import BeautifulSoup

url = "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"

f = urllib.request.urlopen(url)
body = f.read()

soup = BeautifulSoup(body, 'html.parser')

# print(soup.prettify())


def get_ingredients(soup):

	section = soup.find('ul', id='lst_ingredients_1').find_all("span", {"class" : "recipe-ingred_txt"})
	section += soup.find('ul', id='lst_ingredients_2').find_all("span", {"class" : "recipe-ingred_txt"})

	return [ingred.text for ingred in section]



def get_instructions(soup):

	section = soup.find('ol', id="recipe-directions__list").find_all("span", {"class": "recipe-directions__list--item"})
	
	return [item.text for item in section]


def get_prep_time(soup):

	return soup.find('time', {"itemprop": "prepTime"})['datetime']


def get_cook_time(soup):
	return soup.find('time', {"itemprop": "cookTime"})['datetime']


def get_total_time(soup):
	return soup.find('time', {"itemprop": "totalTime"})['datetime']


print(get_prep_time(soup))

