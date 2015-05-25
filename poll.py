import schedule
import time
from threading import Thread
import signal

import thermometer

t = thermometer.ThermometerArray()

def run():
    print("Running periodic task!")
    print t.get_temperatures()

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)   

if __name__ == '__main__':
    schedule.every(10).seconds.do(run)
    thr = Thread(target=run_schedule)
    thr.daemon = True
    thr.start()
    signal.pause()
