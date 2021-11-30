import pandas as pd
import json
from collect_data_package.Modified_Tweet import *
#from collect_data.tweet_collect import *

################ PARTIE PANDAS ####################

# Convertit un status en dataframe en ne gardant que l'information qui nous interesse


def convert_to_df(filename):

    # On ouvre le fichier json
    with open(filename, "r", encoding="utf-8") as fichier:
        mod_tweets = json.load(fichier, object_hook=deserialiseur_tweet)

    row_list = []
    for tweet in mod_tweets:
        row_list.append(serialiseur_tweet(tweet))

    df = pd.DataFrame(row_list)

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['date'])

    return df
