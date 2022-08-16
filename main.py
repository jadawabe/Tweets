import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

raw_tweets = pd.read_json("farmers-protest-tweets-2021-03-5.json", lines = True)
raw_tweets = raw_tweets[raw_tweets['lang'] == 'en']
print("Shape: ", raw_tweets.shape)
raw_tweets.head(5)