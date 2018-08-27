"""Answer to the first question."""

# Import all tokens
from tokens import *

# Import required packages
import matplotlib.pyplot as plt
import re

queries = ['@iiit_hyderabad', '@iiscbangalore']
exports = {}

for query in queries:
    from collections import Counter
    import string
    data = twitter.search(q=query,result_type='mixed',count = 100)

    statuses = data['statuses']
    concat_str = "";
    for post in statuses:
        concat_str = concat_str + " " + post['text']
    concat_str = re.sub(ur"\p{P}+", "", concat_str)
    concat_str = concat_str.lower()
    exports[query] = concat_str
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
    plt.savefig(query + '.png')
