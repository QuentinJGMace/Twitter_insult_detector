from collect_data_package.tweet_raw_collect import *


def collect():
    # On demande à l'utilisateur toutes les infos nécessaires
    filename, username = None, None

    # On demande ce que veux faire l'utilisateur
    reponse1 = input(
        "Voulez-vous collecter les dernières réponses au tweet d'un utilisateur en particulier? (y/n) \n")
    if (reponse1 == 'y'):
        username = input(
            "Quel est l'utilisateur pour lequel vous voulez collecter les réponses? \n N.B : il faut rentrer le nom d'utilisateur c'est à dire un mot de la forme @XXX \n")
        filename = input(
            "Quel est le chemin du fichier dans lequel vous voulez enregistrer ces tweets? \n")

        print("Collecte des données en cours...")

        collect_replies(username, filename)

    queries = []
    reponses2 = input(
        "Voulez-vous collecter des tweets à partir d'un sujet ou d'une liste de sujet? (y/n) \n")
    if (reponses2 == 'y'):

        while(True):
            tmp = input(
                "Entrer un mot lié au sujet de votre collecte \n Si vous n'avez plus de mots à rentrer tappez \"END\" \n")
            if (tmp != "END"):
                queries.append(tmp)
            else:
                break

        filename = input(
            "Dans quel fichier voulez-vous enregistrer ces tweets? \n")

        print("Collecte des données en cours...")

        collect_search(queries, filename)
