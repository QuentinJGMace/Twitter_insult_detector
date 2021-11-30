import tweepy
from collect_data_package.twitter_setup import *
from tweepy.streaming import StreamListener
import time
from collect_data_package.Erreurs import *
from collect_data_package.Modified_Tweet import *

###############Partie Streaming ##############
# Pour chaque stream on dit qu'on collecte les données pour un certain temps avant de fermer le stream

# On stream par défault 5 min d'informations


def get_live_tweets_subject(subject):
    tweets = []

    # On définit notre listener à l'intérieur de la fonction pour pouvoir directement ajouter les messages reçus à la liste replies
    class StdOutListener(StreamListener):

        # On surcharge la fonction init pour ajouter une notion de temps
        def __init__(self, time_limit=300):
            self.start_time = time.time()
            self.limit = time_limit
            super(StdOutListener, self).__init__()

        # Pour arrêter le stream au bout d'un certain temps on doit renvoyer False dans on_status
        def on_status(self, status):
            if (time.time() - self.start_time) < self.limit:
                tweets.append(status)
                return True
            else:
                return False

        def on_error(self, status):
            if str(status) == "420":
                print(status)
                print(
                    "You exceed a limited number of attempts to connect to the streaming API")
                return False
            else:
                return True

    # On initialise l'API
    twitter_api = twitter_setup()
    listener = StdOutListener()

    # On crée le stream
    stream = tweepy.Stream(auth=twitter_api.auth, listener=listener)
    stream.filter(track=[subject])

    # On veut retourner les tweets avec seulement les informations qui nous interesse
    mod_tweets = []
    for tweet in tweets:
        mod_tweets.append(Modified_Tweet(tweet.text, (tweet.created_at).isoformat(), tweet.id, len(
            tweet.text), '@' + tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count))

    return mod_tweets
