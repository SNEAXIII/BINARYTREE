class Noeud:
    """noeud d'un arbre binaire"""
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d


#Exercice 1
"""
A l'oral
"""

#Exercice 2
"""
  fonction qui renvoie le rang de l'élément e si e est présent dans l et None si non
  entrées : e (int), L(list)
  sortie : rez (int, None)
"""
"""
def dicho(e,l):
  premier = 0
  dernier = len(l)-1
  while dernier != premier :
    m = (dernier + premier) // 2
    if e > l[m] :
      premier = m+1
    else :
      dernier = m-1
  if e == l[dernier] :
    rez = dernier
    return rez
  else : return None

liste = [5,10,12,17,32,45,89,122,236,245,310,397,520]
print(dicho(17,liste))
print(dicho(18,liste))
"""
#Exercice 3
"""
1. GIB, CON, REZ, AER
2.17576
3.car c'est un arbre parfait


#Exercice 4

1. il y a 5 arbres binaires possible
2. peigne gauche -> ordre décroissant / peigne droit -> ordre croissant


#Exercice 5

lecture par le parcours InFixe
arbre 1 : 1 - 2 - 3 - 4
arbre 2 : 1 - 2 - 3 - 4 aussi

"""

#Exercice 6

def test(attendu, obtenu):
    print(attendu == obtenu)


def appartient(e, arb):
    #recherche si e est un élément de l'ABR arb

    if arb is None:
        return False

    if e < arb.valeur:
        return appartient(e, arb.gauche)

    if e > arb.valeur:
        return appartient(e, arb.droit)

    return True


#Vous pourrez tester votre algorithme avec

abr1 = Noeud(Noeud(Noeud(None, 5, None), 2, Noeud(None, 3, None)), 4,Noeud(None, 5, None))

#Exercice 7


def ajoute(e, arb):
    #modifie l'arbre non vide en ajoutant l'élément e à celui-ci ou bien renvoie un noeud avec e comme racine à partir d'un arbre vide
    if arb is None:
        return Noeud(None, e, None)

    if e > arb.valeur:
        if arb.droit is None:
            arb.droit = Noeud(None, e, None)
        else:
            ajoute(e, arb.droit)
    elif arb.gauche   is None:
        arb.gauche = Noeud(None, e, None)
    else:
        ajoute(e, arb.gauche)


monArbre = Noeud(Noeud(None, 2, Noeud(None, 4, None)), 5, Noeud(None, 7, None))
monArbre = ajoute(13, monArbre)

"""
4. abr = None -> ajoute(8,arb) -> ajoute(5,arb) -> ajoute(4,arb) -> ajoute(7,arb) -> ajoute(12,arb)

5. monArbre=ajoute(13,monArbre) -> on affecte à monArbre uniquement la feuille qu'on ajoute, donc on complète mon Arbre, mais vu qu'on lui dit de devenir "ajoute" il supprime l'arbre et n'enregistre que la feuille "13"

"""
#Exercice 8
"""

def ajouteV2(e, arb):
    if arb is None:
        return Noeud(None, e, None)

    if e > arb.valeur:
        return Noeud(arb.gauche, arb.valeur, ajouteV2(e, arb.droit))
    else:
        return Noeud(ajouteV2(e, arb.gauche), arb.valeur, arb.droit)

"""
#Exercice 9


class ABR:
    """arbres binaires de recherches"""
    def __init__(self):
        self.racine = None

    def ajouter(self, e):
        if self.racine is None:
            self.racine = Noeud(None, e, None)
        else:
            ajoute(e, self.racine)

    def ajoutemulti(self,*args):
      for a in args:
        self.ajouter(a)

    def ajoutetuple(self,args):
      for a in args:
        self.ajouter(a)

    def hauteur(self):
        #méthode qui calcul la hauteur de l'arbre
        if self.racine is None:
            return 0
        return 1 + max(self.hauteur(self.racine.gauche),self.hauteur(self.racine.droit))
    
    def taille(self):
        #nombre de noeuds de arb
        if self.racine is None:
            return 0
        return 1 + self.taille(self.racine.gauche) + self.taille(self.racine.droit)

    def InFixe(self):
        #méthode qui affiche les éléments de a lors d'un parcours infixe
        if self.racine is None:
            return None
        self.Infixe(self.racine.gauche)
        print(self.racine.valeur,end=",")
        self.Infixe(self.racine.droit)
"""
#Exercice 10

1. Le plus petit élément se trouve le plus à gauche dans un arbre
3. c'est une complexité en 0()
"""
#question 2 de l'exercice 10
def minimum(abr):
    #méthode qui renvoie la plus petite valeur de l'arbre
    if abr.racine is None:
        return None
    minimum(abr.gauche)
    return abr.valeur

#Exercice 11

def ajouteV3(abr,e):

    if abr is None:
        return Noeud(None, e, None)

    if abr.valeur == e:
        return abr

    if e > abr.valeur:
        return Noeud(abr.gauche, abr.valeur, ajouteV3(abr.droit,e))
        
    else:
        return Noeud(ajouteV3(abr.gauche,e), abr.valeur, abr.droit)
    """
    def afficher(self):
        #méthode qui affiche un arbre
        if self.racine is None:
            return ''
        print('(',end='')
        self.afficher(self.racine.gauche)
        print(str(self.valeur),end='')
        self.afficher(self.racine.droit)
        print(')',end='')
    """
def affiche(arb):
  if arb is None:
    return ''
  print('(',end='')
  affiche(arb.gauche)
  print(str(arb.valeur),end='')
  affiche(arb.droit)
  print(')',end='')

affiche(ajouteV3(abr1,6))

#Exercice 12

def compte(e, abr):
    if abr is None :
        return 0

    if abr.valeur == e :        
        return 1 + compte(e, abr.gauche) + compte(e, abr.droit)
    return compte(e, abr.gauche) + compte(e, abr.droit)

abr2 = Noeud(Noeud(Noeud(None, 5, None), 5, Noeud(None, 3, None)), 4, Noeud(None, 5, None))

compte(5, abr2)

#Exercice 13 -> exercice à rendre

def remplir(abr,tab):
    #méthode qui affiche les éléments de a lors d'un parcours infixe
    if self.racine is None:
        return None
    self.Infixe(self.racine.gauche)
    print(self.racine.valeur,end=",")
    self.Infixe(self.racine.droit)