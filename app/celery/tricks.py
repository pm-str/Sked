import sys
from datetime import datetime
from time import sleep
from urllib import request

url = sys.argv[1]
print("url: {}\ndatetime now: {}\n".format(url, datetime.today().isoformat(sep=' ')[:19]))
counter = 0
while True:
    counter += 10
    try:
        with request.urlopen(url, timeout=5) as f:
            print("status code: {}\ndatetime now: {}\n".format(f.getcode(), datetime.today().isoformat(sep=' ')[:19]))
    except Exception as r:
        print("was happened exception: {}\ndatetime now: {}\n".format(r, datetime.today().isoformat(sep=' ')[:19]))
    sleep(10)

