class Noeud:
    """noeud d'un arbre binaire"""

    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

#Exercice 8 : def __eq__

    def _eq_(self,other):
      if self.gauche == other.gauche and self.valeur == other.valeur and self.droit == other.droit :
        return True
      return False

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
        return None
    parcoursInfixe(arb.gauche)
    print(arb.valeur,end=",")
    parcoursInfixe(arb.droit)

#on vérifie le script effectué manuellement
def parcoursPrefixe(arb):
  if arb is None :
    return None
  print(arb.valeur,end=",")
  parcoursPrefixe(arb.gauche)
  parcoursPrefixe(arb.droit)
    
def parcoursPostfixe(arb):
  if arb is None :
    return None
  parcoursPostfixe(arb.gauche)
  parcoursPostfixe(arb.droit)
  print(arb.valeur,end=",")

arb_exo_7 = Noeud(Noeud(Noeud(None,3,Noeud(None,4,None)),1,None),2,Noeud(None,5,None))

##Exercice 7

def affiche(arb):
  if arb is None:
    return ''
  print('(',end='')
  affiche(arb.gauche)
  print(str(arb.valeur),end='')
  affiche(arb.droit)
  print(')',end='')
  
print(affiche(arb_exo_7))
print(arb_exo_7 == arb_exo_7)

##Exercice 9

def parfait(h):
  assert type(h) == int and h>=0, "La hauteur est un entier positif"
  if 
  Noeud(parfait(h-1))

def peigneGauche(h):pass

def peigneDroit(h):pass