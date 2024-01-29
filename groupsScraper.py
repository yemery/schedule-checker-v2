from lxml import html
from bs4 import BeautifulSoup
import requests


def getGr():
    URL = "https://www.nticrabat.com/"
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    select= BeautifulSoup(str(soup.find('select', { "id" : "coursera-front-search-banner-input" })), 'html5lib')
    grList=[]
    for i in select.find_all('option')[1:]:
        # print(i.text,i.attrs['value'])
        grList.append({'id':i.attrs['value'],'value':i.text})
    # print(grList)
    return grList
if __name__ == "__main__":
    getGr()