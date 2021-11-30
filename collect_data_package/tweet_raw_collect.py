import tweepy
from collect_data_package.twitter_setup import *
from tweepy.streaming import StreamListener
import time
from collect_data_package.Erreurs import *
import json
import pandas as pd
from collect_data_package.Modified_Tweet import *

# Retourne une liste de tweets à partir d'une liste de requêtes donnée


def get_tweets_from_search_queries(queries):

    # On doit renvoyer une liste des tweet correspondant aux requêtes
    tweets = []
    twitter_api = twitter_setup()
    # Pour chaque querie on va faire une recherche
    for x in queries:
        try:
            nv_tweets = twitter_api.search(x, language="english", count=100)
            tweets += nv_tweets
        except error.TweepError:
            return (False, TWEEP_ERROR)

        except error.RateLimitError:
            return (False, RATE_LIMIT_ERROR)
        tweets += twitter_api.search(x)

    return tweets


# Collecte les tweets sous forme brut qui sont des réponses données récemment à une personne passée en argument
def get_replies_to_user(user):
    replies = []

    # On ouvre l'api
    api = twitter_setup()

    # On cherche l'id des derniers tweets de l'utilisateur pour avoir acces à ses réponses
    tweet_id = []
    try:
        tweets = api.user_timeline(id=user, count=2)
        for tweet in tweets:
            tweet_id.append(str(tweet.id))
    except tweepy.error.TweepError:
        return (False, 2)
    except tweepy.error.RateLimitError:
        return(False, 3)

    for tweet in tweepy.Cursor(api.search, q='to:'+user, result_type='recent', timeout=1000).items(200):
        # in_reply_to_status_id_str est une string! logique!
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str in tweet_id):
                replies.append(tweet)
    return replies


# Renvoie les derniers retweets d'un tweet d'un utilisateur donné
def get_retweets_of_user(user):
    retweets = []

    # On ouvre l'api
    api = twitter_setup()

    # On cherche l'id du dernier tweet du candidat pour avoir acces a ses réponses
    tweets = []
    tweet_id = []
    try:
        tweets = api.user_timeline(id=user, count=30)
    except tweepy.error.TweepError:
        return (False, 2)
    except tweepy.error.RateLimitError:
        return(False, 3)

    for tweet in tweets:
        retweets += api.retweets(tweet.id, 5)
    return retweets

# Si on détecte un tweet insultant, il peut sans doute être interessant de voir quels ont été les retweets de ce tweet


def get_retweets_of_tweet(tweet):
    return api.retweets(tweet.id, 10)

# Fais une synthèse de toutes les fonctions précédentes pour collecter les tweets et les enregistrer dans un fichier .json
# On ne s'occupe pour l'instant pas du streaming

# Renvoie les tweets modifiés


def collect_replies(username, filename):
    mod_tweets = []
    replies = get_replies_to_user(username)
    for tweet in replies:
        mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
            tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

    store_tweets(mod_tweets, filename)


def collect_search(queries, filename):
    mod_tweets = []
    searchQ = get_tweets_from_search_queries(queries)

    for tweet in searchQ:
        mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
            tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

    store_tweets(mod_tweets, filename)

########Obsolète##########


def collect_tweets(queries, filename, subject="", username=""):
    mod_tweets = []

    # On collecte les tweet par recherche
    if (queries != []):
        searchQ = get_tweets_from_search_queries(queries)

        for tweet in searchQ:
            mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
                tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

    # Fonctions propres à l'username, c'est pour ça qu'on vérifie qu'il est non vide
    if (username != ""):
        replies = get_replies_to_user(username)
        for tweet in replies:
            mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
                tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

        rts = get_retweets_of_user(username)
        for tweet in rts:
            mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
                tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

# Permet de stocker une liste de tweets dans un fichier json


def store_tweets(mod_tweets, filename):
    # On les dump tous dans le même fichier
    with open(filename, "w", encoding="utf_8") as fichier:

        # Note, il faut bien dump toute la liste dans le fichier et pas les éléments 1 par 1 sinon ça ne fonctionne pas
        json.dump(mod_tweets, fichier, default=serialiseur_tweet)

    return mod_tweets
