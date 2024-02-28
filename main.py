from scheduleChecker import scheduleChecker
import schedule
import time
schedule.every(10).minutes.do(scheduleChecker())

while True:
    schedule.run_pending()
    time.sleep(1)
    
   