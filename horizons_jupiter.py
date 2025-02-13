from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from astropy.time import Time
import numpy as np


def compute_error(sim_x, sim_y, sim_z, ref_x, ref_y, ref_z):
    # Calcul direct des distances sans empiler les positions
    distances_sim = np.sqrt(sim_x**2 + sim_y**2 + sim_z**2)
    distances_ref = np.sqrt(ref_x**2 + ref_y**2 + ref_z**2)

    # En pourcentage
    error = np.abs((distances_sim - distances_ref) / distances_ref) * 100
    # Retourne l'erreur moyenne et le tableau d'erreurs
    return np.mean(error), error


def init(dt, start_date, end_date):
    print("Initialisation des parametres...")
    step_size = f'{dt}d'  # Pas de temps d'un jour

    # Creation d'un objet Horizons pour Jupiter
    obj = Horizons(id='599',
                   location='@sun',
                   epochs={
                       'start': start_date,
                       'stop': end_date,
                       'step': step_size
                   })

    # Recuperation des vecteurs de position et de vitesse
    vec = obj.vectors()

    # Extraction des coordonnees heliocentriques (en UA)
    x, y, z = np.array(vec['x'], dtype=float), np.array(
        vec['y'], dtype=float), np.array(vec['z'], dtype=float)
    vx, vy, vz = np.array(vec['vx'], dtype=float), np.array(
        vec['vy'], dtype=float), np.array(vec['vz'], dtype=float)

    # Retourner directement les tableaux necessaires sans autres manipulations
    return x, y, z, vx, vy, vz


def plot_results(x, y, z, sim_x, sim_y, sim_z, start_date, end_date, do_plot):
    print("Affichage des resultats...")

    # Calcul de l'erreur moyenne, mais ne le faire que si necessaire
    erreur_moyenne, erreurs = compute_error(sim_x, sim_y, sim_z, x, y, z)

    if do_plot:
        # Affichage des trajectoires
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')

        nbr_simply = 50  # Reduction de la frequence d'echantillonnage pour alleger les graphiques
        # Trajectoire fournie par Horizons
        ax.plot(x[::nbr_simply],
                y[::nbr_simply],
                z[::nbr_simply],
                marker='o',
                linestyle='-',
                label='Jupiter Trajectory (Horizons)',
                rasterized=True)

        # Trajectoire simulee avec Euler
        ax.plot(sim_x[::nbr_simply],
                sim_y[::nbr_simply],
                sim_z[::nbr_simply],
                marker='.',
                linestyle='--',
                color='green',
                label='Simulated Trajectory (Euler)',
                rasterized=True)

        # Ajout d'un point pour representer le Soleil (position (0,0,0))
        ax.scatter(0,
                   0,
                   0,
                   color='orange',
                   marker='*',
                   s=200,
                   label='Soleil',
                   rasterized=True)

        # Legendes et etiquettes
        ax.set_xlabel('X (UA)')
        ax.set_ylabel('Y (UA)')
        ax.set_zlabel('Z (UA)')
        ax.set_title(
            f'Trajectoire Heliocentrique de Jupiter ({start_date} - {end_date})'
        )

        plt.legend()
        plt.show()

    # Affichage de l'erreur moyenne
    print(
        f"Erreur relative moyenne de la simulation Euler par rapport aux donnees Horizons : {erreur_moyenne:.4f} %"
    )
    if erreur_moyenne < 5:
        print(
            "Vous avez reussi l'erreur moyenne est inferieure à 5% ! Bravo 🎉")

    return erreur_moyenne
