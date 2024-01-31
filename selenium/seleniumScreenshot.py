import time
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
load_dotenv()

def screenshotSchedule(group):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  
    driver = uc.Chrome(options=chrome_options)
    url=f"{os.getenv('URL')}?groupe={group}"
    driver.get(url)
    path=f"screenshots/{group}.png"
    driver.get_screenshot_as_file(path)
    driver.quit()
    
# if __name__ == "__main__":
#     screenshotSchedule(214)