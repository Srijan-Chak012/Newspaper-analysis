import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import nltk

nltk.download('punkt')
nltk.download('stopwords')

import string

filename = "toi.txt"
infile = open(filename, "r", encoding='utf8')
text = infile.read()
infile.close()

import sys

from nltk.tokenize import word_tokenize

tokens = word_tokenize(text)
# print(tokens)

words = [word for word in tokens if word.isalpha()]
# print(words)

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
# print(stop_words)

import re

nt = []
for token in words:
    token = re.sub(r'[^\w\s]', '', token)
    nt.append(token.lower())
ns = []
for stoken in stop_words:
    stoken = re.sub(r'[^\w\s]', '', stoken)
    ns.append(stoken.lower())

# print(nt)

# print(ns)

cwords = [cword for cword in nt if (cword not in ns)]
# print(cwords)

from nltk.stem import SnowballStemmer

sword = [];
for w in cwords:
    snowball = SnowballStemmer('english')
    sword.append(snowball.stem(w))
# print(sword)

final = {}
for w in sword:
    if (w not in final.keys()):
        final[w] = 1;
    else:
        final[w] = int(final[w]) + 1

# import pprint
# pprint.pprint(final)
scounts = dict(sorted(final.items(), key=lambda item: item[1], reverse=True))
for w in scounts.keys():
    print(w + ' : ' + str(final[w]))

# print("Done")
limit = 35  # number of words to plot
keys = list(scounts.keys())[0:limit]
items = [scounts[key] for key in keys]
plt.figure(figsize=(10, 5))
sns.barplot(x=items, y=keys, alpha=0.8)

plt.title("Top Words Overall")
plt.ylabel("Words", fontsize=12)
plt.xlabel("Counts", fontsize=12)
#plt.show()
plt.savefig("wire_bar.png")

wordcloud = WordCloud(width=800, height=800,
                      background_color='#bd8b02',
                      min_font_size=10).generate(" ".join(sword))

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("wire_cloud.png")