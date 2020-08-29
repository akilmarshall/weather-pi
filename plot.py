import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import weatherpi.database as db

plt.style.use('seaborn')

# get the time series data from the database

foo = db.get_all_temperatures()

dates = [a for a,_ in foo]
temps = [(b*1.8) + 32 for _, b in foo]

plt.plot_date(dates, temps)
plt.tight_layout()
plt.savefig('plot.png')
