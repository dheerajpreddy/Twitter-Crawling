"""Answer to fifth question."""

from time import sleep
from datetime import datetime
from textblob import TextBlob
import json, csv
import matplotlib.pyplot as plt

f = open( '../data/research_iiscbangalore_tweets.csv', 'rU' )
reader = csv.DictReader( f, fieldnames = ( "null", "id","created_at","retweet_count","text" ))
data = json.dumps( [ row for row in reader ] )
tweets = json.loads(data)
keyword = 'research'
polarity_list = []
numbers_list = []
number = 1

for i in range(1, len(tweets)):
    analysis = TextBlob(tweets[i]['text'])
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
