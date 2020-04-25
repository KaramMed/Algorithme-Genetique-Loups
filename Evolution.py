from Loup import Loup
import itertools
from itertools import tee
from random import randint
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)





# fonction qui va faire la selection a un ensemble de loups
def selection_naturelle(loups) :
    # trier selon le nb de genes a 0 au genome ( on veut garder les plus blancs )
    liste = loups
    liste_trie = list()
    liste_trie = sorted(liste, key=lambda x: x.nombre_zero(), reverse=True)

    # on va mtn prendre la moitié de la liste ( les survivants )
    taille = 0
    for l in liste_trie :
        taille = taille + 1
    moitie = taille / 2
    ss = itertools.islice(liste_trie,int(moitie)+1)
    survivants = list()
    for s in ss :
        survivants.append(s)

    return survivants


# methode pour faire créer des nouvelles individus ( les enfants )
def crossover(loups) :
    # on va prendre 2 elements par 2
    liste_par_deux = list()
    for l1,l2 in pairwise(loups) :
        liste_par_deux.append((l1,l2))


    nv_liste = list() # la liste des enfants


    for l1,l2 in liste_par_deux :
        # le premier on tire de lui la moitié des premiers genes
        premier_moitie = l1.genome[:2]
        # le deuxieme on tire de lui la moitié des derniers genes
        deuxieme_moitie = l2.genome[2:]
        # on combine pour avoir un nouvel invidivu
        nouveau_loup = Loup("",premier_moitie+deuxieme_moitie) # concatenation des deux
        # on l'ajoute a la liste
        nv_liste.append(nouveau_loup)

    #print(' faire enfants : ')
    #for l in nv_liste:
    #    print(l.genome)

    # on fait la mutation des nouveaux enfants
    nv_liste = mutation(nv_liste)

    #print(' enfants apres mutation : ')
    #for l in nv_liste:
    #    print(l.genome)

    return nv_liste


# methode qui fait la mutatio
def mutation(loups) :
    # pour chaque element on va muter un caractere par hazard
    nv_liste = list()
    for l in loups :
        nv_l = Loup("",l.genome) # on cree un nv
        # on genere un index
        i = randint(0,len(nv_l.genome)-1)
        # on crée un nouveau genome muté
        if nv_l.genome[i] == '1' :
            nv_l.genome = nv_l.genome[:i]+'0'+nv_l.genome[i+1:]
        if nv_l.genome[i] == '0' :
            nv_l.genome = nv_l.genome[:i]+'1'+nv_l.genome[i+1:]
        # on l ajoute a la liste
        nv_liste.append(nv_l)


    return nv_liste



# Main test
l1 = Loup("wolfi","1100")
l2 = Loup("","1011")
l3 = Loup("","1110")
l4 = Loup("","1111")
l5 = Loup("","1011")
l6 = Loup("","0000")
l7 = Loup("","0001")
l8 = Loup("","1011")

liste = list()
liste.append(l1)
liste.append(l2)
liste.append(l3)
liste.append(l4)
liste.append(l5)
liste.append(l6)
liste.append(l7)
liste.append(l8)



i=0
gen = liste
while(i<50) :
    selection = selection_naturelle(gen)
    enfants = crossover(selection)
    selection = selection + enfants
    gen = selection
    print(' generation ',i)
    for s in selection :
        print(s.genome," : ",s.couleur())
    i = i+1

