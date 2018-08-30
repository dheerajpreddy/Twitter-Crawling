"""Answer to second question."""

# Import required packages

import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud, STOPWORDS

stop_words = set(STOPWORDS)

with open('../data/iisc_data.json') as f:
    data = json.load(f)

statuses = data['statuses']
concat_str = "";
for post in statuses:
    concat_str = concat_str + " " + post['full_text'] # concatenate all tweets into one string

wordcloud = WordCloud(width = 800, height = 800,
            background_color ='white',
            stopwords = stop_words,
            min_font_size = 10).generate(concat_str) # Form the wordcloud, remove stopwords as well
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig('../outputs/'+'output_b_IISC'+'.png')
