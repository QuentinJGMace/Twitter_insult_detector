from db_load import *
from ai_usage import *
from collect_data import *
from display_data.display_tendance_color import *
from display_data.display_tendance_tweet import *
import pandas as pd

reponse = input(
    "Voulez vous collecter des données vous-même? (y/n) \n N.B: Si c'est la première utilisation, il faut répondre yes pour avoir une base de données de tweets\n")

if (reponse == 'y'):
    collect()

filename = input("Depuis quel fichier voulez-vous lire vos données? \n N.B: Si vous venez de collecter des données il faut entrer le même chemin que celui où vous avez enregistrer vos données\n  N.B: Il faut répondre 'y' soit à cette question soit à la suivante \n")

# On charge les données dans un dataframe
df = convert_to_df(filename)
# On classifie d'abord chaque tweet selon qu'il soit positif négatif ou neutre
df["type_text"] = pos_neg_tweets(df)

# Puis on classifie plus précisément chaque tweet à l'aide de la deuxième IA
types_insult = insult_type_tweet(df)
toxic = []
severe_toxic = []
obscene = []
threat = []
insult = []
identity_hate = []

for elem in types_insult:
    toxic.append(elem[0])
    severe_toxic.append(elem[1])
    obscene.append(elem[2])
    threat.append(elem[3])
    insult.append(elem[4])
    identity_hate.append(elem[5])

df['toxic'] = toxic
df['severe_toxic'] = severe_toxic
df['obscene'] = obscene
df['threat'] = threat
df['insult'] = insult
df['identity_hate'] = identity_hate

display_tendance_anime(df)
display_tendance_anime_insult(df)
