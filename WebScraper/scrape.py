#import other classes
from format import *
from URLfind import *
import requests

#BeutifulSoup import for reading HTML
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

#recipe_scrapers  import for pulling actual recipe
from recipe_scrapers import scrape_me


URLlist = []
URLlist.append("https://www.allrecipes.com/")
visitedList = []
scraper = Sitemap(URLlist, visitedList)
scraper.readPageLinks()
scraper.clean()
#scraper.printURLlist()
exit()








#scrape url [add function to find url's / generate]
for x in range(10000, 99999):
    scraper = scrape_me('https://www.allrecipes.com/recipe/' + str(x) + '/')
    print(str(x) + ":   " + scraper.title())
    
exit() 

ingredients = scraper.ingredients()
nutrients = scraper.nutrients()
recipe_name = scraper.title()

ingredient_list = Format(ingredients)
simplified_ingredient = ingredient_list.individualIngredients()
print(recipe_name)
print(simplified_ingredient)

#Pull specific ingredient data [add function to parse gathered data]

#Format data

#Push to csv