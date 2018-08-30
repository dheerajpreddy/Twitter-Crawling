"""Get all tweets of a user that have the word 'research' in it."""
import pandas as pd

df = pd.read_csv('../data/iiscbangalore_tweets.csv')
df2 = df[df['text'].str.contains("research")==True]
df2.to_csv('../data/research_iiscbangalore_tweets.csv')
