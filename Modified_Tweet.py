import tweepy
import datetime
# Une classe qui épure un peu les objets pour ne retenir que ce qui nous interesse
# Parce que un tweet brut c'est vraiment illisible


class Modified_Tweet:

    def __init__(self, _text, _date, _id, _len, _username, _retweet_count, _favorite_count):
        self.text = _text
        self.date = _date
        self.id = _id
        self.username = _username
        self.retweet_count = _retweet_count
        self.favorite_count = _favorite_count
        self.len = _len

# Cette fonction va nous permettre de convertir un modified_tweet en json


def serialiseur_tweet(obj):
    if (isinstance(obj, Modified_Tweet)):
        return {"__class__": "Modified_Tweet",
                "id": obj.id,
                "date": obj.date,
                "len": obj.len,
                "text": obj.text,
                "username": obj.username,
                "retweet_count": obj.retweet_count,
                "favorite_count": obj.favorite_count}
    raise TypeError(repr(obj) + "n'est pas sérialisable oskur")

# Permet de lire un json et de le convertir en ModifiedTweet


def deserialiseur_tweet(obj_dict):
    if "__class__" in obj_dict:
        if obj_dict["__class__"] == "Modified_Tweet":
            return Modified_Tweet(obj_dict['text'], obj_dict['date'], obj_dict['id'], obj_dict['len'], obj_dict['username'], obj_dict['retweet_count'], obj_dict['favorite_count'])
    return objet
