from lxml import html
from bs4 import BeautifulSoup
import requests
from utils import scheduleScraper
from db_conn import conn_db
from utils import dict_diff

def scheduleChecker():
    db=conn_db()
    if db!=None:
        groups=db.groups.find()
        for group in groups:
            groupName=group['name']
            # print(groupName)
            # print(scheduleScraper(groupName))
            # print(dict_diff(db.schedules.find_one({"groupeName": f"{groupName}"},{"classes":1,'_id':0}).get('classes'),scheduleScraper(groupName)))
            scraped_schedule=scheduleScraper(groupName)
            diff_dict_checker=dict_diff(db.schedules.find_one({"groupeName": f"{groupName}"},{"classes":1,'_id':0}).get('classes'),scraped_schedule)
            
            
            
            
            
            
            
            # if diff_dict_checker!=None:
            #     db.schedules.update_one({"groupeName": f"{groupName}"},{"$set": { "classes":scraped_schedule }})
            
            
            # print(db.schedules.find_one({"groupeName": f"{groupName}"},{"classes":1,'_id':0}))
            # print("*******\n")
            
        # print(db.groups.find_one())
       
        
        # print([db.schedules.find_one({"groupeName": "214"},{"classes":1,'_id':0})])
        # print(db.schedules.find_one({"groupeName": "214"},{"classes":1,'_id':0}).get('classes'))
        # print(scheduleScraper(214))

           
            
    
    
if __name__ == "__main__":
    scheduleChecker()
   