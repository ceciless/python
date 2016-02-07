# -*-coding:Latin-1 -*
# Etude Triangle de Sierpinski
import numpy as np              # pour la manipulation de matrice
import pylab as pl              # pour la manipulation graphique

# Methode retournant le triangle de pascal
def Pascal(n=2):
    """ Triangle de pascal
    cf. wikipedia http://fr.wikipedia.org/wiki/Triangle_de_Pascal
    """
    c = np.zeros((n,n), dtype="int64") # Pour manipuler des 'gros' chiffres
    c[0,0] = 1
    for i in range(1,n):
        c[i,0] = 1
        for j in range(1,i):
            c[i,j] = c[i-1,j-1] + c[i-1,j]             
        c[i,i] = 1
            
    return np.array(c)

# Methode de sierpinski
def Sierpinski(data,ax):
    taille = np.shape(data) 
    P = np.zeros((taille[0],taille[1]))
    for i in range(taille[0]):
        for j in range(taille[1]):
            #P[i,j] = (data[i,j]%2)
            #if P[i,j] != 0:
            #    ax.scatter(i,j, c='r', marker='o')                
            if  data[i,j]%2== 1:
                P[i,j]= 1
                ax.scatter(i,j, c='r', marker='o')
    return P
    
###############################################################################
# Methode main
if __name__ == "__main__":
    print("Test Triangle de Sierpinski")
    
    n = 128
    triangle = Pascal(n)
    #print triangle
    #print np.shape(triangle)

    # Triangle de Sierpinski et affichage
    fig = pl.figure()           # Creation d'une figure 
    ax  = fig.add_subplot(111)  # Creation d'une 'zone' pour l'affichage     
    graphe = Sierpinski(triangle, ax)
    pl.show()
    
    # la version 'light'
    (x,y)=np.where(triangle%2)
    pl.figure()
    pl.scatter(x,y, marker='o')
    pl.show()