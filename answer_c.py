"""Answer to the third question."""

# Import all tokens
from tokens import *
import time
from datetime import datetime
import matplotlib.pyplot as plt
import collections

queries = ['@iiit_hyderabad', '@iiscbangalore']
data = twitter.search(q=queries[1],result_type='mixed',count = 100)
# x = json.dumps(data)
statuses = data['statuses']
dates = {}

for post in statuses:
    dateData = time.strptime(post['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    dateData = datetime.fromtimestamp(time.mktime(dateData))
    # date = datetime.strptime(dateData, '%b %d %Y %I:%M%p')
    date = dateData.replace(hour=0, minute=0, second=0, microsecond=0)
    # x.append(date)
    if date.strftime("%Y-%m-%d") in dates:
        dates[date.strftime("%Y-%m-%d")] = dates[date.strftime("%Y-%m-%d")] + 1
    else:
        dates[date.strftime("%Y-%m-%d")] = 1

x = []
y = []
od = collections.OrderedDict(sorted(dates.items()))
for k, v in od.iteritems():
    x.append(k)
    y.append(v)
# xAxis = dates.keys()
# yAxis = dates.values()
plt.plot(x, y)
plt.savefig('dates' + '.png')
