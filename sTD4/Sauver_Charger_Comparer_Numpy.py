# -*-coding:Latin-1 -*
# etude Sauver charger comparer des données
import numpy as np              # pour la manipulation de matrice à la matlab 
  
###############################################################################
# Methode main
if __name__ == "__main__":
    print("Test du module Numpy")
    
    # Creation d'un tableau aleatoire A : de taille (N,M) entre [a,b]
    N = 2  # Nombre de lignes
    M = 5  # nombre de colonnes
    a = 1  # Borne inf de l'intervalle
    b = 5  # Borne sup de l'intervalle
    A = (b-a)*np.random.random((N,M)) + a 
    
    # la problématique de la copie d'une variable
    print "la copie de A=B"
    print A[0,0]      
    AA = A          # AA et A pointent vers le même objet !!!!!!!!!!!
    print AA is A   # logique !!! ;-)
    print "modification de AA"
    AA[0][0] = 0
    print AA is A
    print AA[0,0], A[0,0]
    
    print "copie de A dans BB"
    BB = np.copy(A) # La solution !!!!! ;-) BB et A sont deux objets distincts
    print BB is A
    print "modification de BB"
    BB[0][0] = 10
    print BB[0,0], A[0,0]
    # points2 = points.T ou .transpose()
    
    # Affichage console sur la matrice A et autres petits trucs
    print "Etude sur A"
    print type(A)  
    print A[:][:]       # ou A[:,:]
    print A[0][0]
    print A[1,1]
    print A[:][1]
    print np.min(A)     # Calcul la valeur min de A
    print np.max(A)     # Calcul la valeur max de A
    print np.size(A)    # Nombre d'éléments de A
    print np.shape(A)   # Dimension de A
    print np.shape(A.T) # Dimension de A' 
    # Sauvegarde dans un fichier 
    np.savetxt("Fichier_A.txt",A) 
    # Chargement du fichier texte
    B = np.loadtxt("Fichier_A.txt") 
    # Affichage console sur la matrice B
    print "Etude sur B"
    print type(B)
    print B[0][0]
    print B[1,1] 
    # Etude difference entre A et B
    C = A==B    # C: Matrice boolean (True, False si elements de A egale elements de B)
    print "Etude sur C"    
    print C
    print C.all() # Permet de verifier si tous les elements sont True dans C
    
    print "Modification de B et recherche de l'element"
    B[1,3]=0.01 # Modification d'un élément de B
    C = A==B   # test des deux matrices A et B
    print C.all() # Test si tous les elements sont identiques !
    print C.any() # Test si au moins un elements est identique !
    
    indice= np.where(A!=B) # Retour les elements differents
    print indice    
    ind_li = indice[0]
    ind_col= indice[1]
    print ind_li[0], ind_col
    print A[ind_li, ind_col]
    print B[ind_li, ind_col]