#import other classes
from format import *

#BeutifulSoup import for reading HTML
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

#recipe_scrapers  import for pulling actual recipe
from recipe_scrapers import scrape_me


#scrape url [add function to find url's / generate]
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
ingredients = scraper.ingredients()
nutritional = scraper.nutrients()

ingredient_list = Format(ingredients)
ingredient = ingredient_list.individualIngredients()
print(ingredient)

#Pull specific ingredient data [add function to parse gathered data]

#Format data

#Push to csv