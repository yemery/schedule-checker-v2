from bs4 import BeautifulSoup
import requests
from utils import scheduleScraper
from dbConn import conn_db
from utils import dict_diff
from seleniumScreenshot import screenshotSchedule
from discordAlerts import sendAlert
import json
def scheduleChecker():
    db=conn_db()
    if db!=None:
        groups=db.groups.find()
        for group in groups:
            groupName=group['name']
          
            scrapedSchedule=scheduleScraper(groupName)
            diffDictChecker=dict_diff(db.schedules.find_one({"groupeName": f"{groupName}"},{"classes":1,'_id':0}).get('classes'),scrapedSchedule)
            print(diffDictChecker)
            if diffDictChecker!=None:
                screenshotSchedule(groupName)
                # think about adding message contains changes written ! later prb was the structure of dict returned
                message=""
                sendAlert(groupName,message)

            
        
        
       
        
            
            
            # if diffDictChecker!=None:
            #     db.schedules.update_one({"groupeName": f"{groupName}"},{"$set": { "classes":scrapedSchedule }})
            
   


           
            
    
    
