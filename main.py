class Noeud:
    """noeud d'un arbre binaire"""
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

#Exercice 8 : def __eq__

"""
      "A"
     /   \
   "B"   "D"
   / \   / \
     "C"
     / \

se programme : 
"""
arb = Noeud(Noeud(None,'B',Noeud(None,'C',None)),'A',Noeud(None,'D',None))

##Exercice 3

arb1 = Noeud(Noeud(None,4,None),5,Noeud(None,3,None))

arb2 = Noeud(Noeud(Noeud(None,3,Noeud(None,4,None))),1,None(None,2,Noeud(None,5,None))

##Scripts cours 3.2

def taille(arb):
    """nombre de noeuds de arb"""
    if arb is None:
        return 0
    return 1+taille(arb)

def hauteur(arb):
    """renvoie la hauteur de l'arbre"""
    if arb is None:
        return 
    return 1 + 
    
##Exercice 6 parcours Prefixe et Postfixe
def parcoursInfixe(arb):
    """affiche les éléments de a lors d'un parcours infixe"""
    if arb is None:
        return
    parcoursInfixe(arb.gauche)
    print(arb.valeur,end=",")
    parcoursInfixe(arb.droit)

"""on vérifie le script effectué manuellement"""
def parcoursPrefixe(arb):
    
def parcoursPostfixe(arb):

##Exercice 7

def affiche(arb):
    
##Exercice 9

def parfait(h):

def peigneGauche(h):

def peigneDroit(h):
