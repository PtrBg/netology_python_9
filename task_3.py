from datetime import date, timedelta
import time
import requests

date_to = int(time.mktime(date.today().timetuple()))
date_from = int(time.mktime((date.today() - timedelta(days=1)).timetuple()))
url = f'https://api.stackexchange.com/2.3/questions?fromdate={date_from}&todate={date_to}&tagged=Python&site=stackoverflow'
resp = requests.get(url)
print(resp.json())
