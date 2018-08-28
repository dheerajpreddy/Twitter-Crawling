"""Collect tweets of a particular user."""

import csv, tweepy, pickle

consumer_key = "qiOaRLVPldazXmYmF3IaIQw4L"
consumer_secret = "FAzcCMF1UUyuNuSeddAA1nDJYPeXm6OhaCD084k1t3BZ0HleCY"
access_token = "717220472623071233-oeDgXLyYdqT92Mi06aaAGV7EtSExfKS"
access_token_secret = "tVh6WAqVqJ5Pekb3skPON4OD46dyyBAIGOiWjPkZrtglC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

screen_name = "iiscbangalore"
tweets = []
new_tweets = api.user_timeline(screen_name = screen_name, count=200)
tweets.extend(new_tweets)
oldest = tweets[-1].id - 1

while len(new_tweets) > 0:
	new_tweets = api.user_timeline(screen_name = screen_name,count=200, max_id=oldest)
	tweets.extend(new_tweets)
	oldest = tweets[-1].id - 1

outtweets = [[tweet.id_str, tweet.created_at, tweet.retweet_count, tweet.text.encode("utf-8")] for tweet in tweets]
with open('../data/' + '%s_tweets.csv' % screen_name, 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at", "retweet_count","text"])
	writer.writerows(outtweets)
