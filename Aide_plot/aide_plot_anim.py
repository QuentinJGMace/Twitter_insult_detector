import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# si ça déconne il faut vérifier le settings.json

# paramètres quelconques
n = 5
dt = 0.005  # dt va être le pas temporel de l'animation
k = 2*np.pi  # juste un vecteur d'onde pour faire boucler l'animation et l'accélèrer
t = np.linspace(0, 2*np.pi, 100)  # la plage d'angles du paramétrage


fig = plt.figure()  # initialise la figure
line, = plt.plot([], [])
plt.xlim(-1, 1)
plt.ylim(-1, 1)


def init():  # semble définir l'état initial du plot, ie un plot vide
    line.set_data([], [])
    return line,


def animate(i):  # enlever les ''' là où il faut pour obtenir le plot de la fonction encadrée
    '''R = (1/2)*(np.cos(k*i*dt+np.pi)+1)
    x = R*np.cos(t)
    y = R*np.sin(t)'''
    '''R = (1/2)*(np.cos(k*i*dt+np.pi)+1)
    x = (R/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.cos(t)
    y = (R/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.sin(t)'''
    phi = i*dt*k
    x = (1/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.cos(t)*np.cos(phi) - \
        (1/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.sin(t)*np.sin(phi)
    y = (1/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.sin(t)*np.cos(phi) + \
        (1/3)*(1+np.cos(n*t)+(np.sin(n*t))**2)*np.cos(t)*np.sin(phi)
    line.set_data(x, y)
    return line,


def anim_fleur():  # fonction qui plot tout en animant
    animation.FuncAnimation(
        fig, animate, init_func=init, frames=200, blit=True, interval=20, repeat=True)  # frames c'est le nombre d'images qu'on aura
    # interval c'est l'interval temporel (notre temps) qu'il y a
    # repeat ça fait recommencer l'animation quan elle se termine
    plt.show()


anim_fleur()
