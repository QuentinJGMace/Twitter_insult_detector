import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
# import fonction qui donne si un tweet est positif ou negatif


# Cette fonction a pour but de présente les taux de positivité, négativité et neutralité d'un ensemble de tweets
def display_PosiNegNeutre(data):

    # data est un ensemble de tweets non datés auxquels sont associés un caractère positif, négatif ou neutre
    Nbr_tweet = len(data)

    # on initialise la liste des tendances en chaines de caractères

    Noms_tendances = ['ratio_positif', 'ratio_negatif', 'ratio_neutre']
    nombre_cat = len(Noms_tendances)

    # on crée une liste "bouclée" sur elle même pour indiquer les axes du graphe radar
    Ratios = calcul_Ratios_pandas(data)

    # on crée la liste des angles des axes "bouclée" sur elle mêm aussi
    Angles = [np.pi/6+2*np.pi*n/nombre_cat for n in range(nombre_cat)]
    Angles.append(Angles[0])

    # on pinitialise le plot avec une projection polaire
    plt.figure(figsize=(30, 30))
    ax = plt.subplot(111, projection='polar')

    # on donne la position et la couleur des axes ainsi que la taille de leur déscription
    plt.xticks(Angles[:-1], Noms_tendances, color='grey', size=10)

    # on donne certaines valeurs remarquables de rayon du cercle à indiquer ainsi que la limite du graphe
    plt.yticks([0.25, 0.5, 0.75, 1, max(Ratios)], ["0.25", "0.5", "0.75", "1", str(max(Ratios))],
               color="grey", size=7)
    plt.ylim(0, max(Ratios))

    # on plot les valeurs obtenues
    ax.plot(Angles, Ratios, linewidth=1, linestyle='solid',
            color='red', label='ratios de tendance pour '+str(Nbr_tweet)+' tweets')
    plt.legend(bbox_to_anchor=[1.5, 1])

    # on rempli la figure obtenue pour la rendre plus lisible
    ax.fill(Angles, Ratios, 'red', alpha=0.1)
    plt.title(
        "graphe radar du taux de positivité, négativité et neutralité de l'ensemble de tweets", fontweight="bold")
    plt.show()


# Cette fonction a pour but de présente les taux de positivité, négativité et neutralité d'un ensemble de tweets
def display_categories(data):

    # data est un ensemble de tweets non datés auxquels sont associés un caractère positif, négatif ou neutre
    Nbr_tweet = len(data)

    # on initialise la liste des tendances en chaines de caractères

    Noms_tendances = ['toxic',
                      'obscene', 'insult', 'identity hate']
    nombre_cat = len(Noms_tendances)

    # on crée une liste "bouclée" sur elle même pour indiquer les axes du graphe radar
    Ratios = calcul_Ratios_pandas_type(data)

    # on crée la liste des angles des axes "bouclée" sur elle mêm aussi
    Angles = [np.pi/4+2*np.pi*n/nombre_cat for n in range(nombre_cat)]
    Angles.append(Angles[0])

    # on initialise le plot avec une projection polaire
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, projection='polar')

    # on donne la position et la couleur des axes ainsi que la taille de leur déscription
    plt.xticks(Angles[:-1], Noms_tendances, color='grey', size=10)

    # on donne certaines valeurs remarquables de rayon du cercle à indiquer ainsi que la limite du graphe
    plt.yticks([0.25, 0.5, 0.75, 1, max(Ratios)], ["0.25", "0.5", "0.75", "1", str(max(Ratios))],
               color="grey", size=7)
    plt.ylim(0, max(Ratios))

    # on plot les valeurs obtenues
    ax.plot(Angles, Ratios, linewidth=1, linestyle='solid',
            color='red', label='ratios de tendance pour '+str(Nbr_tweet)+' tweets')
    plt.legend(bbox_to_anchor=[1.5, 1])

    # on rempli la figure obtenue pour la rendre plus lisible
    ax.fill(Angles, Ratios, 'red', alpha=0.1)
    plt.title(
        "graphe radar du taux de positivité, négativité et neutralité de l'ensemble de tweets", fontweight="bold")
    plt.show()


data = pd.DataFrame({'tweets': ['salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut'], 'type_text': [
                    'toxic', 'toxic', 'severe_toxic', 'insult', 'positif', 'positif', 'positif', 'positif', 'negatif', 'neutre', 'neutre', 'neutre', 'neutre', 'neutre', 'negatif', 'negatif', 'neutre', 'negatif']})
# on définit une fonctionnalité d'affichage de l'évolution de la tendance d'un ensemble de tweets
# l'idéal serait que cet ensemble de tweets soit rangé dans l'ordre chronologique


def display_tendance_anime(data):
    Nbr_tweet = len(data)
    # on définie une variable globale liste_Ratios qui contiendra une liste de quadruplets [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif]
    global liste_Ratios
    liste_Ratios = liste_Chrono_Ratio(data)

    # On nomme les axes du graphe et on les positionne avec des angles.
    Noms_tendances = ['ratio_positif', 'ratio_negatif', 'ratio_neutre']
    Angles = [np.pi/6+2*np.pi*n/3 for n in range(3)]
    Angles.append(Angles[0])

    # On initialise une figure matplotlib qui s'ouvre avec une taille convenable
    fig = plt.figure(figsize=(30, 30))

    # On initialise un graphe polaire
    ax = fig.add_subplot(111, projection='polar')

    # On donne un nom aux axes
    plt.xticks(Angles[:-1], Noms_tendances, color='grey', size=10)

    # On fait apparaitre des valeurs remarquables de rayon
    # Le rayon du graphe correspond au ration de la tendance: positif, negatif ou neutre
    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.5", "0.75"],
               color="grey", size=7)
    ax.set_ylim(0, 1)

    # On plot un graphe qui napparait pas pour donner une legende au graphe, je n'ai pas trouvé le moyen de faire fonctionner
    # La fonction plt.label
    ax.plot(Angles, [0, 0, 0, 0], linewidth=1,
            color='blue', label='ratios de tendance pour '+str(Nbr_tweet)+' tweets')
    # On replace la légende pour ne pas qu'elle empiète sur le graphe
    plt.legend(bbox_to_anchor=[1.5, 1])

    # On donne un titre au graphe en gras
    plt.title(
        "graphe radar du taux de positivité, négativité et neutralité de l'ensemble de tweets", fontweight='bold')
    l, = ax.plot([], [])

    # à l'intérieur de la fonction, on crée la fonction animate
    # C'est la fonction que le module animation de matplotlib va appeler
    # Elle est définie à l'intérieure de la fonction car elle ne doit avoir qu'un argument
    # qui est un compteur qui sera incrémenté
    def animate(i):

        # liste_Ratios est une liste de listes [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif].
        # On rappel que liste_Ratios est une variable globale pour qu'elle puisse être utilisée
        # dans la fonction
        global liste_Ratios

        # on prend les ratios à un indice i
        Ratios_Actuels = liste_Ratios[i]

        # on plot cela comme demandé par le module animation
        l.set_data(Angles, Ratios_Actuels)

        return (l,)
    # on appelle la fonction d'animation qui ne se répète pas
    speed = 1e4/Nbr_tweet
    animation.FuncAnimation(
        fig, animate, frames=Nbr_tweet, interval=speed, blit=True, repeat=False)
    plt.show()


# On fait la même fonction qu'au dessus simplement pour plus de cases car c'est pour le type d'insulte
def display_tendance_anime_insult(data):
    Nbr_tweet = len(data)
    # on définie une variable globale liste_Ratios qui contiendra une liste de quadruplets [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif]
    global liste_Ratios
    liste_Ratios = liste_Chrono_Ratio_insult(data)
    # On nomme les axes du graphe et on les positionne avec des angles.
    Noms_tendances = ['ratio_toxic', 'ratio_obscene',
                      'ratio_insult', 'ratio_identity_hate']
    Angles = [np.pi/4+2*np.pi*n/4 for n in range(4)]
    Angles.append(Angles[0])

    # On initialise une figure matplotlib qui s'ouvre avec une taille convenable
    fig = plt.figure(figsize=(30, 30))

    # On initialise un graphe polaire
    ax = fig.add_subplot(111, projection='polar')

    # On donne un nom aux axes
    plt.xticks(Angles[:-1], Noms_tendances, color='grey', size=10)

    # On fait apparaitre des valeurs remarquables de rayon
    # Le rayon du graphe correspond au ration de la tendance: positif, negatif ou neutre
    plt.yticks([2e-1, 4e-1, 6e-1, 8e-1], ["2e-1", "4e-1"],
               color="grey", size=7)
    ax.set_ylim(0, 1)

    # On plot un graphe qui napparait pas pour donner une legende au graphe, je n'ai pas trouvé le moyen de faire fonctionner
    # La fonction plt.label
    ax.plot(Angles, [0, 0, 0, 0, 0], linewidth=1,
            color='blue', label='ratios des types d\'insultes '+str(Nbr_tweet)+' tweets')
    # On replace la légende pour ne pas qu'elle empiète sur le graphe
    plt.legend(bbox_to_anchor=[1.5, 1])

    # On donne un titre au graphe en gras
    plt.title(
        "graphe radar du taux de différents types de messages négatifs", fontweight='bold')
    l, = ax.plot([], [])

    # à l'intérieur de la fonction, on crée la fonction animate
    # C'est la fonction que le module animation de matplotlib va appeler
    # Elle est définie à l'intérieure de la fonction car elle ne doit avoir qu'un argument
    # qui est un compteur qui sera incrémenté
    def animate(i):

        # liste_Ratios est une liste de listes [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif].
        # On rappel que liste_Ratios est une variable globale pour qu'elle puisse être utilisée
        # dans la fonction
        global liste_Ratios

        # on prend les ratios à un indice i
        Ratios_Actuels = liste_Ratios[i]

        # on plot cela comme demandé par le module animation
        l.set_data(Angles, Ratios_Actuels)

        return (l,)
    # on appelle la fonction d'animation qui ne se répète pas
    speed = 1e4/Nbr_tweet
    animation.FuncAnimation(
        fig, animate, frames=Nbr_tweet, interval=speed, blit=True, repeat=False)
    plt.show()

# on définit une fonction qui, à partir de data de type pandas
# renvoie le ratio des tendances


def calcul_Ratios_pandas(data):
    Nbr_tweet = len(data)
    Liste_tendance = list(data['tendance'])
    ratio_positif, ratio_negatif, ratio_neutre = 0, 0, 0

    for k in range(Nbr_tweet):
        if Liste_tendance[k] == 'positif':
            ratio_positif += 1/Nbr_tweet
        elif Liste_tendance[k] == 'negatif':
            ratio_negatif += 1/Nbr_tweet
        elif Liste_tendance[k] == 'neutre':
            ratio_neutre += 1/Nbr_tweet

    Ratios = [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif]
    return Ratios

# On veut calculer le pourcentage des différents types de tweet


def calcul_Ratios_pandas_type(data):
    Nbr_tweet = len(data)
    toxic, obscene, insult, identity_hate = 0, 0, 0, 0

    for index, row in data.iterrows():
        toxic += row['toxic']/Nbr_tweet
        obscene += row['obscene']/Nbr_tweet
        insult += row['insult']/Nbr_tweet
        identity_hate += row['identity_hate']/Nbr_tweet

    Ratios = [toxic, obscene, insult, identity_hate, toxic]
    return Ratios


# on définit une même fonction pour une liste de tendances


def calcul_Ratios_liste(liste_Tendance):
    Nbr_tweet = len(liste_Tendance)
    ratio_positif, ratio_negatif, ratio_neutre = 0, 0, 0

    for k in range(Nbr_tweet):
        if liste_Tendance[k] == 'positif':
            ratio_positif += 1/Nbr_tweet
        elif liste_Tendance[k] == 'negatif':
            ratio_negatif += 1/Nbr_tweet
        elif liste_Tendance[k] == 'neutre':
            ratio_neutre += 1/Nbr_tweet

    Ratios = [ratio_positif, ratio_negatif, ratio_neutre, ratio_positif]
    return Ratios

# Cette fonction est une amélioration d'une première version test
# à partir de data sous forme pandas, elle renvoie une liste des ratios des tendances
# dans l'odre chronologique.
# Par exemple, si on a 10 tweets triés par ordre chronologiques et qu'un tendance est associée à chacun,
# la liste contiendra les ratios de tendance pour : le premier tweet, l'ensemble {premier tweet, deuxième tweet}
# l'ensemble {premier, deuxième, troisième}.
# cette fonction va donc nous montrer l'évolution des tendances d'un ensemble de tweets


def liste_Chrono_Ratio(data):

    # on initialise no données et des grandeurs
    Nbr_tweet = len(data)
    liste_Tendance = list(data['type_text'])

    # la liste_Ratios sera la liste renvoyée
    liste_Ratios = []
    ratios = [0, 0, 0]

    # cette fonction a pour but de réduire la complexité de notre objectif
    # on ne va lire qu'un fois la liste des tendances et non pas n fois
    # on devrait passer d'une complexité quadratique à une complexité linéaire
    for step in range(Nbr_tweet):

        # on regarde la dernière liste ratios qu'on avait
        # on multiplie les ratios par le nombre de tweets qu'il y avait à l'étape d'avant
        # on obtient juste une liste de nombres de tweets ayant une certaine tendance
        for i in range(3):
            ratios[i] *= step

        # on fait le test de tendance pour le nouvel élément de la liste de tendance
        # on ajoute 1 tweet
        tendance_Actuelle = liste_Tendance[step]
        if tendance_Actuelle == 'positif':
            ratios[0] += 1
        elif tendance_Actuelle == 'negatif':
            ratios[1] += 1
        elif tendance_Actuelle == 'neutre':
            ratios[2] += 1

        # on divise par le nouveau nombre de tweets pris en compte pour obtenir
        # des ratios
        for j in range(3):
            ratios[j] *= 1/(step+1)

        # on boucle les ratios pour qu'ils puissent être traités par la fonction
        # display_tendance_anime
        ratio_Boucle = ratios[:]+ratios[:1]
        liste_Ratios.append(ratio_Boucle)
    return liste_Ratios


def liste_Chrono_Ratio_insult(data):

    # on initialise no données et des grandeurs
    Nbr_tweet = len(data)
    toxic = list(data['toxic'])
    obscene = list(data['obscene'])
    insult = list(data['insult'])
    identity_hate = list(data['identity_hate'])

    # la liste_Ratios sera la liste renvoyée
    liste_Ratios = []
    ratios = [0, 0, 0, 0]

    # cette fonction a pour but de réduire la complexité de notre objectif
    # on ne va lire qu'une fois la liste des types et non pas n fois
    # on devrait passer d'une complexité quadratique à une complexité linéaire
    for step in range(Nbr_tweet):

        # on regarde la dernière liste ratios qu'on avait
        # on multiplie les ratios par le nombre de tweets qu'il y avait à l'étape d'avant
        # on obtient juste une liste de nombres de tweets classifiés
        for i in range(4):
            ratios[i] *= step

        # On met à jour les ratios
        ratios[0] += toxic[step]
        ratios[1] += obscene[step]
        ratios[2] += insult[step]
        ratios[3] += identity_hate[step]

        # on divise par le nouveau nombre de tweets pris en compte pour obtenir
        # des ratios
        for j in range(4):
            ratios[j] *= 1/(step+1)

        # on boucle les ratios pour qu'ils puissent être traités par la fonction
        # display_tendance_anime
        ratio_Boucle = ratios[:]+ratios[:1]
        liste_Ratios.append(ratio_Boucle)
    return liste_Ratios
