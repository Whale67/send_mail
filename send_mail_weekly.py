from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
import requests

scheduler = BackgroundScheduler()

def get_function():
    url = 'http://www.yourhestia.com/send_weekly_emails'
    r = requests.get(url)
    return(r)

if __name__ == '__main__':
    scheduler.add_job(get_function, 'interval', week=1, start_date='2017-07-04 09:30:00')
    #scheduler.add_job(get_function, 'interval', seconds=10)
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
