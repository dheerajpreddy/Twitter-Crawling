"""Answer to sixth question."""

import pandas as pd

df = pd.read_csv('../data/iiit_hyderabad_tweets.csv')
df2 = df.nlargest(10, 'retweet_count')
# tweets = df2.to_string(columns='text')
RTCountList = df2["retweet_count"].tolist()
tweetList = df2["text"].tolist()

for i in range(0, 10):
    print "Number of reetweets: ", RTCountList[i]
    print tweetList[i]
    print '\n'
