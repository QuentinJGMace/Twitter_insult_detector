import insult_detection_ia.insult_type_ia as insult_ia
import insult_detection_ia.train_and_test_ia as text_ia

from collect_data_package.Modified_Tweet import *

import pandas as pd
import pickle

# Ce fichier sers à utiliser simplement l'IA
# On enregistre notamment l'IA comme variable globale pour pouvoir s'en servir dans tous les fichiers où il est importé

# On lit les fichiers relatifs à l'ia et on les enregistre dans des variables
# Ici c'est pour la classification d'insultes
with open('insult_vectorizer_liblinear', 'rb') as picklefile:
    insult_v = pickle.load(picklefile)

with open('insult_classifier_liblinear', 'rb') as picklefile:
    insult_clf = pickle.load(picklefile)

# Là c'est la même chose pour la classification de texte
with open('text_vectorizer', 'rb') as picklefile:
    text_v = pickle.load(picklefile)

with open('text_classifier', 'rb') as picklefile:
    text_clf = pickle.load(picklefile)


# On définie aussi les fonctions pour classifier les tweets
# Retourne une liste qui donne pour chaque tweets s'il est positif négatif ou neutre
def pos_neg_tweets(df):

    # On extrait d'abord les textes des différents tweets
    textes = []
    for index, tweet in df.iterrows():
        textes.append(tweet['text'])

    # Ensuite on convertit les textes en vecteurs avec le bon vectorizer
    text_vectors = text_v.transform(textes)

    # On peut enfin donner une classification des tweets
    return text_clf.predict(text_vectors)


# Même fonction mais cette fois ci pour donner le type d'insulte
# Le résultat renvoyé est sous la forme d'une liste de liste de 0 ou 1 pour représenter :
# [toxic, severe_toxic, obscene, threat, insult, identity_hate]
def insult_type_tweet(df):

    # On extrait d'abord les textes des différents tweets
    textes = []
    for index, tweet in df.iterrows():
        textes.append(tweet['text'])

    # Ensuite on convertit les textes en vecteurs avec le bon vectorizer
    text_vectors = insult_v.transform(textes)

    # On peut enfin donner une classification des tweets
    return insult_clf.predict(text_vectors)
