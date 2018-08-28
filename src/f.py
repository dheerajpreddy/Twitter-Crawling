"""Answer to sixth question."""

import pickle

file = open('../data/iiit_hyderabad.p', 'rb')
tweets = pickle.load(file)
print type(tweets[0])
