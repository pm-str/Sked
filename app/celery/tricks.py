from urllib import request
from datetime import datetime
from time import sleep
import sys

url = sys.argv[1]
print("url: {}\ndatetime now: {}\n".format(url, datetime.today().isoformat(sep=' ')[:19]))
while True:
    try:
        with request.urlopen(url, timeout=5) as f:
            print("status code: {}\ndatetime now: {}\n".format(f.getcode(), datetime.today().isoformat(sep=' ')[:19]))
    except Exception as r:
        print("was happened exception: {}\ndatetime now: {}\n".format(r, datetime.today().isoformat(sep=' ')[:19]))
    sleep(10)

