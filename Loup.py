
# classe pour representer l'individu loup

class Loup:
    # faut que le genome soit de taille 4
    def __init__(self,nom,genome):
        self.nom = nom
        self.genome = genome


    # methode pour le nb de genes a 0 au genome ( on veut garder les plus blancs )
    def nombre_zero(self):
        return self.genome.count('0')

    # methode qui change un gene du genome
    def change_gene(self,i,j,val):
        self.genome[i:j] = val

    # methode qui retourne la couleur
    def couleur(self):
        # on crée la couleur selon le genom
        nb_un = self.genome.count('1')
        nb_zero = self.genome.count('0')
        if nb_un == 4:
            couleur = " noir "
        if nb_un == 3:
            couleur = " envers noir "
        if nb_un == 2 and nb_zero == 2:
            couleur = " gris "
        if nb_zero == 3:
            couleur = " envers blanc "
        if nb_zero == 4:
            couleur = " blanc "
        return couleur
