import numpy as np
import horizons_jupiter


def euler_method(x0, y0, z0, vx0, vy0, vz0, dt, n_steps):
    """
    Simule la trajectoire de Jupiter autour du Soleil en utilisant la méthode d'Euler.

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

    # Ici c'est à vous de jouer, il faut déterminer la trajectoire de Jupiter autour du soleil.
    # Bon courage et hésitez pas à me contacter si vous êtes bloqué :)

    return sim_x, sim_y, sim_z


# Date du début de la simulation
start_date = '2010-01-01'
# Date de la fin de la simulation
end_date = '2025-02-13'
# pas de temps en nombre de jours
dt = 1

# Dans cette fonction on initialise les paramètres ne vous en occupez pas!
x, y, z, vx, vy, vz = horizons_jupiter.init(dt, start_date, end_date)

# Dans cette fonction on initialise les paramètres ne vous en occupez pas!
sim_x, sim_y, sim_z = euler_method(x[0], y[0], z[0], vx[0], vy[0], vz[0], dt,
                                   len(x))

horizons_jupiter.plot_results(x, y, z, sim_x, sim_y, sim_z, start_date,
                              end_date)
