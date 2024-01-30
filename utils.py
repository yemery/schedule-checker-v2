from lxml import html
from bs4 import BeautifulSoup
import requests
import json
from deepdiff import DeepDiff

def scheduleScraper(group):
    payload={
            'groupe':f'{group}',
        }
    URL = "https://www.nticrabat.com/emploi/emp.php"
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