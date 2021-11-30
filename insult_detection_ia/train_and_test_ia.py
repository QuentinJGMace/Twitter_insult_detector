from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pickle
import os


def train_and_test_Ai():

    # On initialise ce dont on a besoin
    classes = ['positif', 'negatif', "neutre"]
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    # On remplie les différents trucs à tester
    for curr_class in classes:
        dirname = curr_class + ".txt"
        with open(os.path.join("bases_de_données/bases_de_données_exploitables/", dirname), "r", encoding="utf-8") as f:
            content = f.readlines()
            i = 0
            l = len(content)
            for line in content:
                if (i <= 0.9 * l):
                    train_data.append(line)
                    train_labels.append(curr_class)
                else:
                    test_data.append(line)
                    test_labels.append(curr_class)
                i += 1

    # On transforme les données brutes (phrases) en vecteurs pour pouvoir faire du machine learning avec
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # On entraine notre IA avec la training data
    classifier_liblinear = svm.LinearSVC()
    classifier_liblinear.fit(train_vectors, train_labels)

    # On enregistre le vectorizer dans un fichier pour pouvoir le réutiliser après
    with open('../text_vectorizer', 'wb') as picklefile:
        pickle.dump(vectorizer, picklefile)

    # On enregistre le modèle dans un fichier pour pas avoir a re-train à chaque fois
    with open('../text_classifier', 'wb') as picklefile:
        pickle.dump(classifier_liblinear, picklefile)

    # On voit ce que notre IA donne sur la testing data
    prediction_liblinear = classifier_liblinear.predict(test_vectors)

    # On print les résultats pour voir les performances de notre IA
    print(classification_report(test_labels, prediction_liblinear))
