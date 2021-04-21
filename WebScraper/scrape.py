#import other classes
from format import *
from URLfind import Sitemap as URLfind
from URLSQL import manageURL as URLSQL
import requests

#BeutifulSoup import for reading HTML
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

#recipe_scrapers  import for pulling actual recipe
from recipe_scrapers import scrape_me

#database imports 
import sqlite3 

test = URLSQL()
test.connectTable()
exit()

#initialize lists
URLlist = []
URLlist.append("https://www.allrecipes.com/")
visitedList = []
scraper = URLfind(URLlist, visitedList)



while len(scraper.URLlist) < 300:
    scraper.readPageLinks()
    scraper.clean()
    scraper.stats()

scraper.printvisitedList()
print("------------------------------------------")

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

