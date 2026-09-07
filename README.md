# Paléoclimatologie : Reconstruction des températures historiques

## Présentation
Ce dépôt contient le traitement des jeux de données, les analyses statistiques et les modèles d'apprentissage automatique utilisés pour reconstruire les températures régionales historiques (Japon, France et Finlande) au cours du dernier millénaire. En analysant des proxys naturels et historiques sur le long terme, on identifie les tendances climatiques locales, les anomalies et les corrélations à l'échelle de l'hémisphère nord.

## Proxys et sources de données
* **Japon** : 
  * Dates de floraison des cerisiers à Kyoto (821–2021).
  * Dates de gel et de dégel (*Omiwatari*) du lac Suwa.
  * Dendrochronologie (cernes d'arbres) près du lac Suwa.
* **France** :
  * Dates des vendanges à Beaune et en Europe (1354–2024).
  * Dendrochronologie en Europe.
* **Finlande** :
  * Dates de dégel de la rivière Tornionjoki (1693–2013).

## Méthodologie et modèles
* **Traitement des données** : Conversion des registres historiques en jeux de données `.csv` standardisés et lissage par moyennes mobiles (10 à 40 ans).
* **Modèles de reconstruction** :
  * **Modèles physiques et statistiques** : Régressions linéaires et modélisation physique d'Arrhenius.
  * **Réseaux de neurones** : Perceptrons multicouches (TensorFlow) entraînés sur les périodes de chevauchement avec les mesures de températures instrumentales modernes.
* **Analyse comparative** : Corrélations interrégionales, détection de ruptures et mise en parallèle avec les événements climatiques historiques (ex. éruptions volcaniques, Petit Âge Glaciaire).

## Structure du dépôt
```text
.
├── base_de_donnee/    # Jeux de données CSV standardisés (proxys et séries de températures)
├── analyse/           # Scripts Python pour les corrélations, régressions et réseaux de neurones
├── Figure/            # Figures générées, graphiques et courbes lissées
├── ressources/        # Références bibliographiques, articles et documentation
└── README.md          # Documentation principale du projet
