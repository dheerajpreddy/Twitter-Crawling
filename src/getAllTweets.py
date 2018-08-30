"""Collect tweets of a particular user."""

import csv, tweepy

consumer_key = "nZSdk3QfF4SuO5I1assGAaZOm"
consumer_secret = "NmjFsFohlC0Trr34ghc1nnZc3JsPnjJUSlzCZ11nGkJ3QtIYWD"
access_token = "973951591249190912-wsvLdApA3YkcMYqvtKMZNasVa698wUT"
access_token_secret = "AbhkZ86INFeVSjzpCYVBxFjjpjfm6MEOjPuGywoIrOcKt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

screen_name = "iiit_hyderabad"
tweets = []
new_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode='extended')
tweets.extend(new_tweets)
oldest = tweets[-1].id - 1

while len(new_tweets) > 0:
	new_tweets = api.user_timeline(screen_name = screen_name,count=200, max_id=oldest, tweet_mode='extended')
	tweets.extend(new_tweets)
	oldest = tweets[-1].id - 1

outtweets = [[tweet.id_str, tweet.created_at, tweet.retweet_count, tweet.full_text.encode("utf-8")] for tweet in tweets]
with open('../data/' + '%s_tweets.csv' % screen_name, 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at", "retweet_count","text"])
	writer.writerows(outtweets)
