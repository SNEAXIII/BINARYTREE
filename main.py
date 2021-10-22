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

arb1 = Noeud(Noeud(None,4,None),5,Noeud(None,3,None))

##Scripts cours 3.2

def taille(arb):
    """nombre de noeuds de arb"""
    if arb is None:
        return 0
    return 1 + taille(arb.gauche) + taille(arb.droit)

print(taille(arb))

def hauteur(arb):
    #renvoie la hauteur de l'arbre
    if arb is None:
        return 0
    return 1 + max(hauteur(arb.gauche),hauteur(arb.droit))
    
print(hauteur(arb))

##Exercice 6 parcours Prefixe et Postfixe

def parcoursInfixe(arb):
    #affiche les éléments de a lors d'un parcours infixe
    if arb is None:
        return
    parcoursInfixe(arb.gauche)
    print(arb.valeur,end=",")
    parcoursInfixe(arb.droit)

#on vérifie le script effectué manuellement
def parcoursPrefixe(arb):pass
  
    
def parcoursPostfixe(arb):pass
""" 
##Exercice 7

def affiche(arb):pass
    
##Exercice 9

def parfait(h):pass

def peigneGauche(h):pass

def peigneDroit(h):pass
"""