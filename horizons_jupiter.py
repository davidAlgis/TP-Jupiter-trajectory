from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from astropy.time import Time
import numpy as np
from euler_integration import euler_method


def compute_error(sim_x, sim_y, sim_z, ref_x, ref_y, ref_z):
    sim_positions = np.vstack((sim_x, sim_y, sim_z)).T
    ref_positions = np.vstack((ref_x, ref_y, ref_z)).T

    distances_sim = np.linalg.norm(sim_positions, axis=1)
    distances_ref = np.linalg.norm(ref_positions, axis=1)

    error = np.abs((distances_sim - distances_ref) /
                   distances_ref) * 100  # En pourcentage
    return np.mean(
        error), error  # Retourne l'erreur moyenne et le tableau d'erreurs


# Paramètres de l'observation
start_date = '2010-01-01'
end_date = '2025-02-13'
step_size = '1d'  # Pas de temps d'un jour

# Création d'un objet Horizons pour Jupiter
obj = Horizons(id='599',
               location='@sun',
               epochs={
                   'start': start_date,
                   'stop': end_date,
                   'step': step_size
               })

# Récupération des vecteurs de position et de vitesse
vec = obj.vectors()

# Extraction des coordonnées héliocentriques (en UA)
x = np.array(vec['x'], dtype=float)
y = np.array(vec['y'], dtype=float)
z = np.array(vec['z'], dtype=float)

# Extraction des vitesses héliocentriques (en UA/jour)
vx = np.array(vec['vx'], dtype=float)
vy = np.array(vec['vy'], dtype=float)
vz = np.array(vec['vz'], dtype=float)

# Extraction des dates pour l'affichage
dates = Time(vec['datetime_jd'], format='jd').iso

# Paramètres physiques
mu = 0.00029591220828559104  # [UA^3/jour^2] paramètre gravitationnel du Soleil
dt = 1.0  # Pas de temps en jours

# Simulation de la trajectoire avec la méthode d'Euler
sim_x, sim_y, sim_z = euler_method(x[0], y[0], z[0], vx[0], vy[0], vz[0], mu,
                                   dt, len(x))

# Calcul de l'erreur moyenne
erreur_moyenne, erreurs = compute_error(sim_x, sim_y, sim_z, x, y, z)

# Affichage des trajectoires
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Trajectoire fournie par Horizons
ax.plot(x,
        y,
        z,
        marker='o',
        linestyle='-',
        label='Jupiter Trajectory (Horizons)')

# Trajectoire simulée avec Euler
ax.plot(sim_x,
        sim_y,
        sim_z,
        marker='.',
        linestyle='--',
        color='green',
        label='Simulated Trajectory (Euler)')

# Ajout d'un point pour représenter le Soleil (position (0,0,0))
ax.scatter(0, 0, 0, color='orange', marker='*', s=200, label='Soleil')

# Légendes et étiquettes
ax.set_xlabel('X (UA)')
ax.set_ylabel('Y (UA)')
ax.set_zlabel('Z (UA)')
ax.set_title(
    f'Trajectoire Héliocentrique de Jupiter ({start_date} - {end_date})')

# Ajout des annotations aux points de départ et de fin
# ax.text(x[0], y[0], z[0], dates[0], color='red')
# ax.text(x[-1], y[-1], z[-1], dates[-1], color='blue')

plt.legend()
plt.show()

# Affichage de l'erreur moyenne
print(
    f"Erreur relative moyenne de la simulation Euler par rapport aux données Horizons : {erreur_moyenne:.4f} %"
)
