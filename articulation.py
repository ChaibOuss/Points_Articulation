#importer numpy pour le calcul matriciel
import numpy as np
from queue import LifoQueue 
#recuperer le nombre de sommets 
dim = int(input("Veuillez donner le nombre de sommets: \n"))
#initialisation du graphe en utilisant une matrice
graphe = np.arange(dim*dim)
graphe.shape = (dim, dim)
#remplir la matrice
'''
    1) si i et j sont liés => 1
    2) sinon => 0
'''
print("rempissez la matrice ligne par ligne :")
for i in range(0, dim):
    for j in range(0, dim):
        graphe[i,j] = int(input())
print("Le graphe sous forme matricielle : ")
print(graphe)
print("==================================")
#liste connexe contient le numero de la composante connexe
'''
    1)si deux composantes ont le meme numero dans la liste
        ils appertiennent a la meme compsante connexe
    2)sinon ils ne sont pas dans la meme composante
'''
liste_connexe = np.arange(dim)
for i in range(0, dim):
    liste_connexe[i] = 0
'''
    Remplir la liste
'''
cpt_connexe = 0
'''
    on calcule le nombre de composantes connexes en utilisant
    la methode bfs (parcours en largeur)
'''
pile = LifoQueue(maxsize = dim)
for i in range(0, dim):
    if liste_connexe[i] == 0:
        cpt_connexe = cpt_connexe + 1
    pile.put(i)
    j = i
    while pile.qsize() != 0:
        if liste_connexe[j] == 0 :
            liste_connexe[j] = cpt_connexe
            for k in range(0, dim):
                if (graphe[j, k] == 1) and (liste_connexe[k] == 0):
                    pile.put(k)
        j = pile.get()
    
print("la liste connexe des graphes : \n")
print(liste_connexe)
'''
    pour avoir le nombre de composantes connexes
    on supprime chaque fois un sommet et
    on recalcule le nombre de composantes connexes
    si le nombre de composantes connexes augmente
    le point supprimé est ajouté à la liste des 
    compsantes connexes
'''
liste_compare = np.arange(dim)
point_articulation = LifoQueue(maxsize = dim)
for i in range(0, dim):
    liste_compare[i] = 0
for s in range(0, dim):
    cpt_compare = 0
    for i in range(0, dim):
        liste_compare[i] = 0
    for i in range(0, dim):
        if s != i:
            if liste_compare[i] == 0:
                cpt_compare = cpt_compare + 1
            pile.put(i)
            j = i
            while pile.qsize() != 0:
                if liste_compare[j] == 0 :
                    liste_compare[j] = cpt_compare
                    for k in range(0, dim):
                        if k != s:
                            if (graphe[j, k] == 1) and (liste_compare[k] == 0):
                                pile.put(k)
                j = pile.get()
    print(cpt_compare)
    if cpt_compare > cpt_connexe:
        point_articulation.put(s)
#enlever le commentaire pour afficher les points sur la console
'''
print("Les points d'articualtion sont : \n")
while point_articulation.qsize() != 0:
    print(point_articulation.get())
'''
    
#importer graphviz pour visualiser le graphe avec les points d'articulation
from graphviz import Graph
g = Graph('G', filename='articulation.gv')
print("Nombre de points d'articulation : ", point_articulation.qsize())
'''
    les points d'articulation sont schématisés en boite vertes
    les autres points sont schématisés en circles grises
'''
while point_articulation.qsize() != 0:
    g.attr('node', style='filled', color='green', shape='box')
    g.node(str(point_articulation.get()))
g.attr('node', shape = 'ellipse', color='lightgrey')
for i in range(0, dim):
    for j in range(0, i):
        if graphe[i,j] == 1:
            g.edge(str(i), str(j))
g.view()        
