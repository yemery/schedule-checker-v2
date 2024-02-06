from bs4 import BeautifulSoup
import requests
import json
from deepdiff import DeepDiff
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.options import Options
load_dotenv()

def scheduleScraper(group):
    payload={
            'groupe':f'{group}',
        }
    URL = os.getenv('URL')
    r = requests.get(URL,params=payload)
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = BeautifulSoup(str(soup.find_all('table')[-1]), 'html5lib')
    
    schedule=[]
    
    tr = table.find_all("tr")[2:]
    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    classesTime=[
  {"startTime": "08:00", "endTime": "10:00"},
  {"startTime": "10:00", "endTime": "13:00"},
  {"startTime": "13:00", "endTime": "16:00"},
  {"startTime": "16:00", "endTime": "18:00"}
]

    for index,row in enumerate(tr):
        scheduleOfDay=[]
        for i,td in enumerate(row.find_all('td')[1:]):
            professorName = td.get_text(strip=True, separator='\n').split('\n')[0]
            classParent=td.find('a')
            classroom="" if classParent is  None else classParent.text
            isAbsent=td.attrs["bgcolor"]
            scheduleOfDay.append({"professorName":professorName,"isAbsent":isAbsent,"classroom":classroom,"startTime":classesTime[i]["startTime"],"endTime":classesTime[i]["endTime"]})        
        schedule.append({f"{daysOfWeek[index]}":scheduleOfDay})
        
    return schedule



def dict_diff(dataset1,dataset2):
    diff = DeepDiff(dataset1, dataset2, ignore_order=True)
    if not diff:
        return None
    else:
        return diff
    
    
    
def classStatus(bgColor):
    pass

def conn_db():
    try:   
        client = MongoClient(os.getenv("MongoDB_URI"))
        db = client[os.getenv("db_name")]

        return db
    except Exception as e:
            print(f"Error : {e}")
            return None
        
        
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
headers = {
    'Authorization': f'Bot {TOKEN}',
   
}
def screenshotSchedule(group):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  
    driver = uc.Chrome(options=chrome_options)
    url=f"{os.getenv('URL')}?groupe={group}"
    driver.get(url)
    path=f"selenium_Images/screenshots/{group}.png"
    driver.get_screenshot_as_file(path)
    driver.quit()
    
    
def sendAlert(group):
    screenshotSchedule(group)
    imagePath=f"selenium/screenshots/{group}.png"
    
    data = {
    'content': 'Hello, Discord!',
    }
    files = {'file': ('discrod/214.png', open('discord/214.png', 'rb'), 'image/png')}

    response = requests.post(url, headers=headers, data=data,files=files)

    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')

