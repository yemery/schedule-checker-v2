from lxml import html
from bs4 import BeautifulSoup
import requests

from db_conn import conn_db

def scrape_insert_groups():
    URL = "https://www.nticrabat.com/"
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    select= BeautifulSoup(str(soup.find('select', { "id" : "coursera-front-search-banner-input" })), 'html5lib')
    # grList=[]
    db=conn_db()
    if db != None:
        groups = db["groups"]
        for i in select.find_all('option')[1:]:
            # print(i.text,i.attrs['value'])
            db.groups.insert_one({'name':i.attrs['value'],'value':i.text})
            # grList.append({'id':i.attrs['value'],'value':i.text})
    else:
        print('Error')
           
        
if __name__ == "__main__":
    scrape_insert_groups()