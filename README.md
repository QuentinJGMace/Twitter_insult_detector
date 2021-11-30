# Annalyseur de comportement adapté à la plateforme Twitter

## Membres
Hugo Samson, Pierre Labouré, Benoît Le Harivel De Gonneville, Quentin Macé

## Objectif

L'objectif de ce projet est d'observer le comportement des utilisateurs de Twitter. Ceci à l'aide d'une mise en forme visuelle 
qui permet de mieux appréhender les tendances comportementales suivant les thèmes de d'échange, les réponses à un tweet 
en particulier, ou même à l'échelle d'un compte Twitter.
Le projet est axé sur les analyses des tweets à tendance négatifs en permettant de la classifier précisément grâce à plusieurs 
sous catégories différentes.

## Fonctionnalités

Le projet permet à l'utilisateurs de récolter un ensembles de tweets suivant une liste de thèmes qui l'intéresse, ou 
bien les réponses qui peuvent survenir à un tweet en particulier, ou bien encore les tweets d'un compte.
Il lui permet aussi d'enregistrer ces données où il le souhaite.
L'utilisateur peut lui même joindre un fichier .json au dossier du projet s'il souhaite une étude sur un ensemble de tweets déjà fournis et interessant.
Grâce à une intelligence artificielle entraînée par du Machine Learning sur des bases de données, les tweets sont 
ensuite triés en différentes catégories: positif, négatif et neutre.
Si un tweet est négatif, il est de nouveau 
catégorisés (mais cette fois il peut apartenir à différentes catégories) : toxique, obscène, haine identitaire et 
insulte.
Une deuxième intelligence articificielle entrainée sur une base de données différente permet de rafiné ce classement en des catégories différentes.
Ces catégories sont : toxique, obscène, haine identaire et insulte. (Il y a aussi menace et toxique-sévère mais elles ne sont pas utilisées par le reste du programme)
L'utilisateur bénéfieciera d'un affichage dynamique avec deux graphes polaires qui lui permettront d'obtenir le nombre 
de tweets par catégories en fonction du temps écoulé.

## Consignes d'utilisation

-   Il faut d'abord avoir des droits d'accès à l'API twitter. Elles doivent être enregistrées dans un fichier nommé "credentials.py" et contenir les variables globales :
CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'

ACCESS_TOKEN = 'XXX'
ACCESS_SECRET = 'XXX'

Si vous ne disposez pas de l'accès à l'API twitter contactez quentin.mace@student-cs.fr.

-   Ensuite une fois cela fait il faut éxécuter le fichier main.py
    Des instructions dans la console devraient apparaître pour vous demander si vous voulez enregistrer des tweets et sur quel sujet les enregistré.
    Si vous ne disposez pas déjà de base de données de tweet (ce qui est le cas à la première utilisation) vous devez obligatoirement enregistrer des données.

-   Il faut après donner le chemin d'accès du fichier où sont stockés les tweets. Des graphes sont censés s'afficher.

## Améliorations à introduire

Il pourrait être utile de faire une interface graphique plus agréable que des commandes consoles.

Aussi, il faudrait que le logiciel puisse bénéficier de l'analyse de tweets dans différentes langues (autres que l'anglais). Il suffit pour cela de 
compléter les bases de données.

## Contact

quentin.mace@student-cs.fr
hugo.samson@student-cs.fr
pierre.laboure@student-cs.fr
benoit.de-gonneville@student-cs.fr