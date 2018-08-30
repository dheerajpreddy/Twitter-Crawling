"""Answer to the third question."""

import json
import time
from datetime import datetime
import matplotlib.pyplot as plt
import collections

with open('../data/iisc_data.json') as f:
    data = json.load(f)

statuses = data['statuses']
dates = {}

for post in statuses:
    dateData = time.strptime(post['created_at'],'%a %b %d %H:%M:%S +0000 %Y') # get time
    dateData = datetime.fromtimestamp(time.mktime(dateData)) # convert to datetime
    # date = datetime.strptime(dateData, '%b %d %Y %I:%M%p')
    date = dateData.replace(hour=0, minute=0, second=0, microsecond=0) # keep onnly date
    # x.append(date)
    if date.strftime("%Y-%m-%d") in dates:
        dates[date.strftime("%Y-%m-%d")] = dates[date.strftime("%Y-%m-%d")] + 1 # increment value in dict
    else:
        dates[date.strftime("%Y-%m-%d")] = 1 # initialize value in dict

x = []
y = []
od = collections.OrderedDict(sorted(dates.items())) # Sort dates in order
for k, v in od.iteritems():
    x.append(k)
    y.append(v)
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.savefig('../outputs/' + 'output_c_IISC' + '.png')
