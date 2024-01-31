from lxml import html
from bs4 import BeautifulSoup
import requests
from scraper.utils import scheduleScraper
from mongodb.db_conn import conn_db
from scraper.utils import dict_diff

def scheduleChecker():
    db=conn_db()
    if db!=None:
        groups=db.groups.find()
        for group in groups:
            groupName=group['name']
          
            scraped_schedule=scheduleScraper(groupName)
            diff_dict_checker=dict_diff(db.schedules.find_one({"groupeName": f"{groupName}"},{"classes":1,'_id':0}).get('classes'),scraped_schedule)
            print(diff_dict_checker)
            
            
            
            
            
            
            # if diff_dict_checker!=None:
            #     db.schedules.update_one({"groupeName": f"{groupName}"},{"$set": { "classes":scraped_schedule }})
            
   


           
            
    
    
if __name__ == "__main__":
    scheduleChecker()
   