import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import _cm
import matplotlib.animation as animation
from textblob import TextBlob
# import fonction qui donne si un tweet est positif ou negatif


# Cette fonction a pour but de présente les taux de positivité, négativité et neutralité d'un ensemble de tweets
# tout en attribuant une couleur au graphe selon sa polarité
# on calcule la polarité avec textblob
def display_tendance_couleur(tweet, reponses_tweet):

    # data est un ensemble de tweets non datés auxquels sont associés un caractère positif, négatif ou neutre
    Nbr_tweet = len(reponses_tweet)

    # on transforme le tweet original en textblob
    # on lui attribue une polarité modifiée
    # voir la fonction modified_polarity
    tweet_TextBlob = TextBlob(tweet)
    polarity = tweet_TextBlob.sentiment.polarity
    modif_polarity = modified_polarity(polarity)

    # on initialise la colormap brg qui a peu de couleurs lumineuses qui pourraient être dures à voir
    # on prend N=100 pour avoir une large palette de couleurs, il faudra donc donner une modif_polarity
    # comprise entre 0 et 100.
    N = 100
    cmap = plt.get_cmap('brg', N)

    # on initialise la liste des tendances en chaines de caractères
    Noms_tendances = ['ratio_positif', 'ratio_negatif', 'ratio_neutre']

    # on crée une liste "bouclée" sur elle même pour indiquer les axes du graphe radar
    Ratios = calcul_Ratios_pandas(reponses_tweet)

    # on crée la liste des angles des axes "bouclée" sur elle mêm aussi
    Angles = [np.pi/6+2*np.pi*n/3 for n in range(3)]
    Angles.append(Angles[0])

    # on initialise le plot avec une projection polaire
    ax = plt.subplot(111, projection='polar')

    # on donne la position et la couleur des axes ainsi que la taille de leur déscription
    plt.xticks(Angles[:-1], Noms_tendances, color='grey', size=10)

    # on donne certaines valeurs remarquables de rayon du cercle à indiquer ainsi que la limite du graphe
    plt.yticks([0.25, 0.5, 0.75, 1, max(Ratios)], ["0.25", "0.5", "0.75", "1", str(max(Ratios))],
               color="grey", size=7)
    plt.ylim(0, max(Ratios))

    # on plot les valeurs obtenues avec la couleur correspondante
    # on déplace la légende pour ne pas qu'elle gène le graphe
    ax.plot(Angles, Ratios, linewidth=1, linestyle='solid',
            color=cmap(modif_polarity), label='ratios de tendance pour '+str(Nbr_tweet)+' tweets')
    plt.legend(bbox_to_anchor=[0, 1])

    # on rempli la figure obtenue pour la rendre plus lisible
    # le remplissage est presque transparent pour plus de clareté : alpha=0.1
    ax.fill(Angles, Ratios, color=cmap(modif_polarity)[:-1], alpha=0.1)
    plt.title(
        "graphe radar du taux de positivité, négativité et neutralité de l'ensemble de tweets")

    # on crée une colorbar pour lire la polarité
    a = np.array([[]])
    plt.imshow(a, cmap='brg', vmin=-1, vmax=1)
    plt.gca().set_visible(True)
    plt.colorbar()

    plt.show()


réponses = pd.DataFrame({'tweets': ['salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut', 'salut'], 'tendance': [
    'positif', 'negatif', 'neutre', 'negatif', 'positif', 'positif', 'positif', 'positif', 'negatif', 'neutre', 'neutre', 'neutre', 'neutre', 'neutre', 'negatif', 'negatif', 'neutre', 'negatif']})


tweet = "hi"

# cette fonction calcule les ratios de positivité, négativité, neutralité d'un ensemble de tweets
# sous la forme de data de type pandas


def calcul_Ratios_pandas(data):
    Nbr_tweet = len(data)
    Liste_tendance = list(data['type_text'])
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

# La fonction polarity de textblob donne peu de valeurs extrêmes
# on fait donc une dilatation de cette polarité tout en la centrant au milieu de la colormap (d'où le terme +50).
# Avec cette dilatation, la polarité modifiée peut sortir du segment [0,100] qu'on a donné à la colormap,
# On place donc un palier pour ces valeurs


def modified_polarity(polarity):
    dilatation_polarity = 50+75*polarity
    if dilatation_polarity >= 100:
        dilatation_polarity = 100
    elif dilatation_polarity <= 0:
        dilatation_polarity = 0

    # on retourne un entier dans [|0,100|]
    return np.int(dilatation_polarity)
