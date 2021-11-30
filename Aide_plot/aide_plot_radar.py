# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})


# number of variable
categories = list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:


# loc c'est comme pour accèder à une liste
values = df.loc[0].drop('group').values.flatten().tolist()
# drop retire les lignes qu'on ne veut pas
# values ne sort que les valeurs numériques


# on rajoute la première valeur pour boucler le graphique radar
values += values[:1]
values


# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]  # on crée le n simplex avec des angles égaux


# Initialise the spider plot
# ne pas chercher à comprendre, ça plot en polaire
ax = plt.subplot(111, projection='polar')

# Draw one axe per variable + add labels labels yet
# plt.xticks(la laiste des angles rebouclés, le nom des axes, la couleur et la taille des titres)
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
# plt.yticks(liste de où mettre les valeurs et les cercles, liste des noms des valeurs, couleur et taille)
plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.ylim(0, 40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
# rempli le graphe de couleur, alpha correspond à la transparence
ax.fill(angles, values, 'blue', alpha=0.1)

plt.show()
