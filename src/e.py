"""Answer to fifth question."""

from time import sleep
from datetime import datetime
from textblob import TextBlob
import json
import matplotlib.pyplot as plt

with open('../data/iisc_data.json') as f:
    data = json.load(f)

keyword = 'research'
polarity_list = []
numbers_list = []
number = 1

for tweet in data['statuses']:
    analysis = TextBlob(tweet['full_text'])
    analysis = analysis.sentiment
    polarity = analysis.polarity
    polarity_list.append(polarity)
    numbers_list.append(number)
    number = number + 1

axes = plt.gca()
axes.set_ylim([-1, 2])
plt.scatter(numbers_list, polarity_list)
averagePolarity = (sum(polarity_list))/(len(polarity_list))
averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity), fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))
plt.title("Sentiment of " + keyword + " on Twitter")
plt.xlabel("Number of Tweets")
plt.ylabel("Sentiment")
plt.savefig('../outputs/' + 'output_e_IISC' + '.png')
