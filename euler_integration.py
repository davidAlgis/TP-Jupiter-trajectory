import numpy as np


def euler_method(x0, y0, z0, vx0, vy0, vz0, mu, dt, n_steps):
    """
    À Faire : Simule la trajectoire de Jupiter autour du Soleil en utilisant la méthode d'Euler.

    Paramètres :
        x0, y0, z0 (float) : Position initiale en UA.
        vx0, vy0, vz0 (float) : Vitesse initiale en UA/jour.
        mu (float) : Paramètre gravitationnel du Soleil (UA^3/jour^2).
        dt (float) : Pas de temps en jours.
        n_steps (int) : Nombre d'étapes de la simulation.

    Retourne :
        sim_x, sim_y, sim_z (np.ndarray) : Tableaux contenant la trajectoire simulée.
    """
    # Initialisation des tableaux de position
    sim_x = np.zeros(n_steps)
    sim_y = np.zeros(n_steps)
    sim_z = np.zeros(n_steps)

    # Initialisation des tableaux de vitesse
    sim_vx = np.zeros(n_steps)
    sim_vy = np.zeros(n_steps)
    sim_vz = np.zeros(n_steps)

    # A faire déterminer la trajectoire de Jupiter autour du soleil.

    return sim_x, sim_y, sim_z
