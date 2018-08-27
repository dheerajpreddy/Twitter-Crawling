"""Answer to the third question."""

# Import all tokens
from tokens import *
from datetime import datetime

queries = ['@iiit_hyderabad', '@iiscbangalore']
data = twitter.search(q=queries[0],result_type='mixed',count = 100)
# x = json.dumps(data)
statuses = data['statuses']
x = []
y = []
for post in statuses:
    x.append(datetime.strptime(post[0]['created_at'][4:], '%b %d %I:%M%p')
    y.append()
