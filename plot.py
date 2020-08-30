import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests
from datetime import datetime


plt.style.use('seaborn')

url = 'http://192.168.1.102:5000/'
api = f'{url}all_temperatures'
r = requests.get(api)
data = r.json()

slc = slice(None, None, 10)
dates = [x[0] for x in data[slc]]
temps = [x[1] for x in data[slc]]

# change string format into datetime
# date_format = '%a, %m %b %Y %X'
# dates = [datetime.strptime(x[0][-4], date_format) for x in data[slc]]

# convert C -> F
temps = [(1.8 * x) + 32 for x in temps]


plt.xlabel('Time of day')
plt.ylabel('Temperature F')
plt.plot_date(dates, temps)
plt.tight_layout()
plt.show()
# plt.savefig('plot.png')
