"""Answer to fourth question."""

import json
import matplotlib.pyplot as plt

with open('../data/iisc_data.json') as f:
    data = json.load(f)

psize_media_count = 0
url_count = 0

for tweet in data['statuses']:
    if 'extended_entities' in tweet:
        psize_media_count = psize_media_count + 1
    elif 'https://t.co' in tweet['full_text']:
        url_count = url_count + 1

plt.pie([psize_media_count, url_count, len(data['statuses'])-psize_media_count-url_count], explode=(0.1, 0.1, 0), labels=['Media', 'URL', 'Only Text'], colors=['green', 'blue', 'yellow'], autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.savefig('../outputs/'+'output_d_iisc' + '.png')
