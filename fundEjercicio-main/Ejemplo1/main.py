from time import time, sleep
from datetime import datetime
while True:
    now = datetime.now()
    sleep(1)

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)