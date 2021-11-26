##Partie 1 Recherche par dichotomie

#Exercice 1
"""Expliquez le résultat"""


#Exercice 2
def dicho(e,L):


    return

lst = [5,10,12,17,32,45,89,122,236,245,310,397,520]
print(dicho(17,lst))
print(dicho(18,lst))

##Partie 2 : Arbre binaire de recherche

#Exercice 3

#1. (sur feuille)
#2. Combien de villes possède Binarus ?

#3.Expliquez votre réponse


#Exercice 4

#1. Sur feuille
#2. Expliquez votre réponse



##Partie 3 Algorithmes et Arbres Binaires

#Exercice 5 : Expliquez votre réponse



#Exercice 6 : Recherche d'un élément

def appartient(e,arb):
    """recherche si e est un élément de l'ABR arb"""

    if arb is None:
        return

    if e<arb.valeur:
        return

    if e>arb.valeur:
        return

    return

#Vous pourez tester votre algorithme avec
abr1=Noeud(Noeud(Noeud(None,1,None),2,Noeud(None,3,None)),4,Noeud(None,5,None))


#Exercice 7 : Ajout d'un élément

#1. Sur feuille
#2. Complétez l'algorithme ci-dessous

def ajoute(e,arb):
    """modifie l'arbre non vide en ajoutant l'élément e à celui-ci ou bien renvoie un noeud avec e comme racine à partir d'un arbre vide"""
    if arb is None:
        return

    if e>arb.valeur:
        if arb.droit is None:
            arb.droit =
        else:

    elif     is None:
        =


#3. Donnez votre réponse

#4. Ecrire les instructions

#5. Expliquez votre réponse



#Exercice 8 : ajoute V2

#1. Programmez l'algorithme
def ajouteV2(e,arb):


#2. Expliquez votre réponse

#3.a quel est le nombre d'appels

#3.b majoration de la complexité dans le cazs d'un arbre équilibré


#3.c complexité en pire cas.



##Partie 4 : Encapsulation

class ABR:
    """arbres binaires de recherches"""



#Exercice 9 : Complétez la classe avec les méthodes


##Partie 5  : Exercices supplémentaires

#Exercice 10

#1. Programmez la fonction
def minimum(arb):

    return

#2 Quelle est la complexité ?


#Exercice 11

def ajouteV2b(arb):

    pass


#Exercice 12


def compte(e,arb):

    pass


#Exercice 13

#1. Modifie le tableau après un parcours InFixe de l'ABR arb

def remplir(arb,tab):

    pass


#2. compléter la classe ABR avec la méthode lister

#3 Programmez la fonction

def triABR(tab):

    pass

#4. Quelle est la complexité ?




