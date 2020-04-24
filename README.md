# Algorithme-Genetique-Loups
Simulation d'un algorithme génétique pour un ensemble d'individus ( Loups ) dans une zone glacial

Loup.py : la classe Loup , dont il dispose d'un nom , d'un genome ( ensemble de genes composés de 1 et 0 ) , et d'une couleur qui depends du genome pour preciser la couleur du loup

Evolution.py : comprends les differents methodes pour simuler l'evolution

selection naturelle() : prends un ensemble d'individus ( loups ) , les trier selon le nombre de genes de la couleur blanche , et retourne la moitié des meilleurs individus classés

crossover() : prends un ensemble d'individus , prends chaque 2 individus et combine leurs genomes pour créer de nouvelles individus enfants , ensuite une mutation et retourne cette liste

mutation() : prends un ensemble d'individus , pour chacun cherche un gene au hazard et l'inverse
