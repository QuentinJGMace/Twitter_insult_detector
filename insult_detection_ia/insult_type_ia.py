import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pickle
import os

from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier

# On liste l'état d'une phrase sous la forme d'un tableau de bolléen de la forme :
# [toxic, sever_toxic, obscene, threat, insult, identity_hate]


# Fonction qui ne sert a rien
def create_listStates(reste):
    if reste == 1:
        return [[0], [1]]
    else:
        res = []
        for state in create_listStates(reste-1):
            res.append([0] + state)
            res.append([1] + state)
        return res


def train_insult_ia_KNN():
    # Un message peut être dans 64 étéats différents en fonction de ses caractéristiques
    classes = create_listStates(6)

    train_data = []
    test_data = []

    train_labels = []
    test_labels = []
    names = ["toxic", "severe_toxic", "obscene",
             "threat", "insult", "identity_hate"]

    pd_file3 = pd.read_csv(r'D:/école/Centrale/Coding_weeks/youtube_insult_detector/bases_de_données/bases_de_données_à_exploiter/neg_comments.csv',
                           sep=',', names=["id", "comment text"]+names, encoding='utf-8')

    i = 0
    l = len(pd_file3.index)

    # On ajoute les données à nos train data et test data
    for index, row in pd_file3.iterrows():
        if i < 0.9 * l:
            train_data.append(row['comment text'])
            label = [row['toxic'], row['severe_toxic'], row['obscene'],
                     row['threat'], row['insult'], row['identity_hate']]

            train_labels.append(label)
        else:
            test_data.append(row['comment text'])
            label = [row['toxic'], row['severe_toxic'], row['obscene'],
                     row['threat'], row['insult'], row['identity_hate']]

            test_labels.append(label)
        i += 1

    # On transforme les données brutes (phrases) en vecteurs pour pouvoir faire du machine learning avec
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # On entraine notre IA avec la training data
    # classifier_liblinear = svm.LinearSVC()
    # classifier_liblinear.fit(train_vectors, train_labels)

    clf = MultiOutputClassifier(KNeighborsClassifier()).fit(
        train_vectors, train_labels)
    predictions = clf.predict(test_vectors)

    # On enregistre le vectorizer dans un fichier pour pouvoir le réutiliser après
    with open('insult_vectorizer', 'wb') as picklefile:
        pickle.dump(vectorizer, picklefile)

    # On enregistre le modèle dans un fichier pour pas avoir a re-train à chaque fois
    with open('insult_classifier', 'wb') as picklefile:
        pickle.dump(clf, picklefile)

    print(classification_report(test_labels, predictions))


def train_insult_ia_liblinear():
    # Un message peut être dans 64 étéats différents en fonction de ses caractéristiques
    classes = create_listStates(6)

    train_data = []
    test_data = []

    train_labels = []
    test_labels = []
    names = ["toxic", "severe_toxic", "obscene",
             "threat", "insult", "identity_hate"]

    pd_file3 = pd.read_csv(r'D:/école/Centrale/Coding_weeks/youtube_insult_detector/bases_de_données/bases_de_données_à_exploiter/neg_comments.csv',
                           sep=',', names=["id", "comment text"]+names, encoding='utf-8')

    i = 0
    l = len(pd_file3.index)

    # On ajoute les données à nos train data et test data
    for index, row in pd_file3.iterrows():
        if i < 0.9 * l:
            train_data.append(row['comment text'])
            label = [row['toxic'], row['severe_toxic'], row['obscene'],
                     row['threat'], row['insult'], row['identity_hate']]

            train_labels.append(label)
        else:
            test_data.append(row['comment text'])
            label = [row['toxic'], row['severe_toxic'], row['obscene'],
                     row['threat'], row['insult'], row['identity_hate']]

            test_labels.append(label)
        i += 1

    # On transforme les données brutes (phrases) en vecteurs pour pouvoir faire du machine learning avec
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # On entraine notre IA avec la training data
    # classifier_liblinear = svm.LinearSVC()
    # classifier_liblinear.fit(train_vectors, train_labels)

    clf = MultiOutputClassifier(svm.LinearSVC()).fit(
        train_vectors, train_labels)
    predictions = clf.predict(test_vectors)

    # On enregistre le vectorizer dans un fichier pour pouvoir le réutiliser après
    with open('insult_vectorizer_liblinear2', 'wb') as picklefile:
        pickle.dump(vectorizer, picklefile)

    # On enregistre le modèle dans un fichier pour pas avoir a re-train à chaque fois
    with open('insult_classifier_liblinear2', 'wb') as picklefile:
        pickle.dump(clf, picklefile)

    print(classification_report(test_labels, predictions))


# Renvoie l'interprétation faite par l'IA (algorithme KNN) sur l'ensemble de phrases passé en argument
def test_ia_KNN(phrases):
    # On enregistre le vectorizer dans un fichier pour pouvoir le réutiliser après
    with open('insult_vectorizer', 'rb') as picklefile:
        vectorizer = pickle.load(picklefile)

    # On enregistre le modèle dans un fichier pour pas avoir a re-train à chaque fois
    with open('insult_classifier', 'rb') as picklefile:
        classifier = pickle.load(picklefile)

    test_vectors = vectorizer.transform(phrases)
    return classifier.predict(test_vectors)

# Renvoie l'interprétation faite par l'IA (liblinear) sur l'ensemble de phrases passé en argument


def test_ia_liblinear(phrases):
    # On enregistre le vectorizer dans un fichier pour pouvoir le réutiliser après
    with open('insult_vectorizer_liblinear', 'rb') as picklefile:
        vectorizer = pickle.load(picklefile)

    # On enregistre le modèle dans un fichier pour pas avoir a re-train à chaque fois
    with open('insult_classifier_liblinear', 'rb') as picklefile:
        classifier = pickle.load(picklefile)

    test_vectors = vectorizer.transform(phrases)
    return classifier.predict(test_vectors)
