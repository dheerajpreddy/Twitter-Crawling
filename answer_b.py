"""Answer to second question."""

# Import the data collected from first answer
from answer_a import exports as data

# Import required packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

stop_words = set(STOPWORDS)

i = 0
for content in data:
    i = i + 1
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stop_words,
                min_font_size = 10).generate(data[content])
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig('wc' + str(i) + '.png')
