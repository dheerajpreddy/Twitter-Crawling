"""Answer to the first question."""

# Import required packages
import matplotlib.pyplot as plt
import re
from collections import Counter
import string
import json
import nltk

def removeStopWords(str):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(str)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    finalStr = ' '.join(x for x in filtered_sentence if x.isalnum())
    return finalStr

with open('../data/iisc_data.json') as f:
    data = json.load(f)

statuses = data['statuses']
concat_str = "";
for post in statuses:
    concat_str = concat_str + " " + post['full_text']
concat_str = removeStopWords(concat_str)
words = concat_str.split()
Counter = Counter(words)
most_frequent = Counter.most_common(20)
x = []
y = []
for i in range(0, len(most_frequent)):
    x.append(most_frequent[i][0])
    y.append(most_frequent[i][1])

plt.figure(figsize=(20, 5))  # width:20, height:5
plt.bar(x, y, align='center', width=0.3)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.savefig('../outputs/'+'output_a_IISC' + '.png')
