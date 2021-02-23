import requests 
import bs4

    
class Sitemap:

    def __init__(self, URLlist, visitedList):
        self.URLlist = URLlist
        self.visitedList = visitedList
        self.domain = URLlist[0]

    def printURLlist(self):
        for link in self.URLlist:
            print(link)

    #Scrape the URLS
    def readPageLinks(self):
        page = requests.get(self.URLlist[0])
        self.URLswitch()
        links = bs4.BeautifulSoup(page.text, 'lxml')
        for link in links.find_all('a', href=True):
            self.URLlist.append(link['href'])
        self.clean
        
    def URLswitch(self):
        self.visitedList.append(self.URLlist[0])
        self.URLlist.remove(self.URLlist[0])

    def clean(self): 
        for link in self.URLlist:
            if self.domain in link:
                print(link)
                self.URLlist.remove(link)
            else:
                print("POOP" + link)

        





