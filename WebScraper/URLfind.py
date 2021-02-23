import requests 
import bs4

    
class Sitemap:

    def __init__(self, URLlist, visitedList):
        self.URLlist = URLlist
        self.visitedList = visitedList
        self.domain = "https://www.allrecipes.com/recipe"

    #iterates through the entire list
    def printURLlist(self):
        for link in self.URLlist:
            print(link)

    #iterates through the visited list
    def printvisitedList(self):
        for link in self.visitedList:
            print(link)


    #Scrape the URLS
    def readPageLinks(self):
        page = requests.get(self.URLlist[0])
        self.URLswitch()
        links = bs4.BeautifulSoup(page.text, 'lxml')
        for link in links.find_all('a', href=True):
            self.URLlist.append(link['href'])
        
    def URLswitch(self):
        self.visitedList.append(self.URLlist[0])
        self.URLlist.remove(self.URLlist[0])

    def clean(self):
        new_list = []
        for link in self.URLlist:
            if self.domain in link[0:len(self.domain)]:
                new_list.append(link)
        self.URLlist = list(set(new_list) - set(self.visitedList))
        
        
    def stats(self):
        print(len(self.URLlist))
        print(len(self.visitedList))




