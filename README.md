# TP2 - Étude de la trajectoire de Jupiter autour du Soleil

Ce dépôt contient le matériel nécessaire pour le TP2 visant à simuler la trajectoire de Jupiter en utilisant la méthode d'intégration d'Euler et à comparer cette simulation avec les données issues de l'outil `Horizons` de la NASA.

## 📂 Contenu du dépôt

Le projet est structuré comme suit :

```
📁 TP-Jupiter-trajectory/
│── 📄 euler_integration.py  # Script à compléter par les étudiants
│── 📄 horizons_jupiter.py   # Script fournissant les données et affichant les résultats
│── 📄 requirements.txt      # Liste des dépendances Python
│── 📄 Enonce-TP2.pdf        # Énoncé du TP
│── 📄 README.md             # Ce fichier
```

## 📥 Installation

### Cloner le dépôt

Pour commencer, récupérer le dépôt sur votre machine :

```bash
git clone https://github.com/davidAlgis/TP-Jupiter-trajectory.git
cd TP-Jupiter-trajectory
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Lancer le TP

Exécutez le script `euler_integration.py` :

```bash
python euler_integration.py
```

Lors du premier lancement, vous devriez voir un graphique affichant uniquement la trajectoire de Jupiter issue de `Horizons` et une erreur de **100%**, indiquant que l'implémentation de la méthode d'Euler est incomplète.

### Modifier et compléter la méthode d'Euler

Dans le fichier `euler_integration.py`, complétez la fonction `euler_method` en suivant les instructions du TP.

L'objectif est d'obtenir une erreur relative inférieure à **5%**.

### Tester différentes valeurs de `dt`

Modifiez la variable `dt` dans `euler_integration.py` et testez avec différentes valeurs (`2`, `5`, `10`). Analysez l'impact sur la précision de la simulation.

## 📖 Références

- [NASA Horizons System](https://ssd.jpl.nasa.gov/horizons/app.html) : Service en ligne pour obtenir des données orbitales précises.
- [Documentation Astroquery](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html) : Documentation sur l'utilisation de `astroquery.jplhorizons`.

