# wordfreq.py
#     Program to analyze the frequency of words in a text file.
from pathlib import Path

import urllib.request as urllib
import pandas as pd
from string import punctuation
from collections import Counter
from time import time
import sys
from pprint import pprint

#url = 'https://medium.com/@TebbaVonMathenstien/the-technology-of-2018-6f32d564255a'
#data =  urllib.urlopen(url).read()

mdata_folder = Path("C:/Users/langzx/Documents")
data = mdata_folder / "data.txt"

word_count = Counter()

with open(data,"r+") as file:
    word_count.update((word for word in file.read().split()))

for word, count in word_count.most_common():
    print (word, count)


#########################

text = """\
From the Graves region within the Bordeaux area of France comes the sweet white dessert wine of Sauternes.  Made predominantly from the Semillon grape, though, there are blended wines from the region that incorporate Sauvignon Blanc and Muscadelle grapes as well. Here is a more detailed link to read about the finer points of Sauternes.
One of the key elements necessary to a fine dessert wine is the effect that Botrytis has on the grape. This Botrytis, or “Noble rot”, as it is called in France, is essential to the development of the sugar and yeast.  Go here to read more about this amazing mold and how it transforms the grape.

The high sugar content and relatively low alcohol make wines from Sauternes very good candidates for long-term storage. Notice in the picture below, how the older wines begin to show more color. White wine gains color as it ages. In another 5 to 10 years the older wines will look like honey.

"""




text = ''.join(c for c in text if c not in punctuation)
#text = ''.join([c for c in text if c not in punctuation])
text_words = Counter(text.split())
text_words.most_common(100)

wordslist = text_words.most_common()
wordslist
## convert tuple to dataframe
wordfredata = pd.DataFrame(list(wordslist))
wordfredata.columns = ['word', 'frequency']

print(wordfredata['frequency'].to_string(index=False))



