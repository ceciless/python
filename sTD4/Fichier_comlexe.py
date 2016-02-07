# -*- coding: Latin-1  -*- 

# importation des modules
import re                           # pour traiter les expressions régulieres
import os
import math
import LatLongUTMconversion as LLUC # permet de définir un alias pour un module
import pylab as py                  # module pour affichage des données

import matplotlib.pyplot as plt         # pour la manipulation graphique 3d
from mpl_toolkits.mplot3d import Axes3D # pour la manipulation graphique 3d

# page web pour affichage 3D : 
# http://matplotlib.sourceforge.net/mpl_toolkits/mplot3d/tutorial.html#d-plots-in-3d

""" Etude des fonctions et modules additionnels
"""
# Methode permettant Test de la presence (ou non) du fichier
def TestOpenFichier(namefile):
    print " -> Test si presence du fichier: ", namefile
    try:
        test_file = file(namefile,"r") # Test la presence du fichier         
        return 1
        
    except IOError:
        print " Ouille ! pas de fichier: ", namefile
        os.system("exit")  # si pas de fichier à charger on quitte le programme
        return 0

    
# Méthode permettant Lecture et traitement du fichier
# Fait appel à la methode TestOpenFichier()
def LectureFichier(namefile):
    """ -> Lecture et traitement du fichier simple data"""
    test_in_file = TestOpenFichier(namefile)
    
    expreg = re.compile("\d+\.\d+ \d+\.\d+ \d+\.\d+ \d+(\.\d+)?") # 4 colonnes de décimales
    data_float = []                     # Liste pour stockage des donnéees
    if test_in_file != 0:   
        print " --> Traitement du fichier"
        
        in_file = open(namefile,"r")    # Ouverture du fichier à la lecture        
        for ligne in in_file:
            
            # Gestion si pas le bon formalisme via une exception
            if expreg.match(ligne):
                data_float.append([float(element) for element in ligne.split()])
            else:
                print " Probleme à la ligne: ", ligne
    
        in_file.close() # Fermeture du fichier à la lecture
    
    return data_float   # Retourne la liste des données en float

# Methode permettant la Lecture et Traitement d'un fichier complexe
# Fait appel à la methode TestOpenFichier()
def lectureFichierComplexe(namefile):
    """ -> Lecture et traitement du fichier complexe data"""
    test_in_file = TestOpenFichier(namefile)
    
    # expression reguliere : ... ,nombre,[N ou S],nombre,[E ou W],... 
    expreg = re.compile("(,)(\d+\.\d+)(,[N-n-S-s],)(\d+\.\d+)(,[E-e-W-w],)")  
    data_float = []                     # Liste pour stockage des donnéees
    indice = 0;
    if test_in_file != 0:
        print " --> Traitement du fichier"
        
        in_file = open(namefile,"r")    # Ouverture du fichier à la lecture        
        for ligne in in_file:
           
            # Traitement de la ligne             
            data_txt = ligne.split(",") # Separation en char via ','
            #print ligne                 # Affichage de la ligne
            #print data_txt              # Affichage des characteres de la ligne
            #print len(data_txt)         # Nombre de characteres sur la ligne
            
            if len(data_txt) ==15:      # La ligne à probablement le bon format si 15 elements
                
                # Traitement de la ligne si nbr de satellites >= 10   
                nbre_satellites = int(data_txt[7])
                if nbre_satellites<10:
                    print "Nombre de satellites inf à 10: ", nbre_satellites, 'à la ligne', indice
           
                else:      
                    result    = re.search(expreg, ligne) # Extraction de l'expression 
                    latitude  = float(result.group(2))   # Coordonnées N-S                  
                    longitude = float(result.group(4))   # Coordonnées E-W
                    altitude  = float(data_txt[9]) + float(data_txt[11]) # pas de test ici ;-(
                    temps     = float(data_txt[1])# Pour avoir le bon format par la suite : temps, lat, long, hauteur
                    
                    #print nbre_satellites   # Nbre de satellites                          
                    #print result.group()    # Chaine de caracteres extraites
                    #print latitude, longitude, altitude
                    #print temps
                    
                    # Stockage des données extraites du fichier 
                    # selon le format : temps, latitude, longitude, hauteur
                    data_float.append([temps, latitude, longitude, altitude])
            
            else:
                print "Probleme sur la ligne: trop courte, ligne : ", indice 
                print ligne

            indice = indice + 1;    # compteur de ligne traité
    
        in_file.close()             # Fermeture du fichier à la lecture
    
    return data_float               # Retourne la liste des données en float

# Methode permettant la conversion des degrés, minutes décimales en degrés décimaux
def dmd_to_dd(dmd):
    """ Conversion GPS deg,min decimal -> deg decimal"""
    deg    = int(math.floor(dmd/100))    
    minute = dmd-deg*100.0
    return deg+minute/60.0

# Methode permettant le triatement des données
# Format d'une ligne : temps(ms), latitude (dmd), longitude (dmd), hauteur(m)
def TraiteData(data_float):
    """ Traitement de l'ensemble du fichier """
    print " -> Conversion des données en UTM"
    coords = [] # Stockage des données UTM
    for line_data in data_float:
        
        # Conversion des données dmd en latitude,longitude
        latitude  = dmd_to_dd(line_data[1])
        longitude = dmd_to_dd(line_data[2])
        
        # Conversion latitude,longitude -> UTM (est, nord)
        # on se trouve dans la zone 23 (port de Brest)
        (zone,est,nord) = LLUC.LLtoUTM(23,latitude,longitude)
        coords.append([line_data[0], est, nord, line_data[3]])
    return coords

# Methode sauvegarde dans un fichier
def SaveData(data, out_name="toto.txt"):
    """ Affichage des données """
    out_file = open(out_name,"w") # ouverture du fichier en ecriture

    for ligne in data:
        for data in ligne:
            out_file.write(str(data)+" ")   # Stockage de la donné en string + " "
        out_file.write("\n")                # Passage à la ligne suivante
    
    out_file.close()            # Fermeture du fichier

# Methode permettant l'affichage des données
# la données d'entrée à le meme format que dans les fichiers txt
# il sera necessaire de transposé les données pour extraire les colonnes 
def AffichageData(data):
    """ Methodes d'affichages"""
    data_col = zip(*data)   # Pour extraire facilement les colonnes
    
    print "Affichage: Exemple 1"
    py.figure()
    py.plot(data_col[1], data_col[2], 'r')
    py.xlabel("Est")
    py.ylabel("Nord")
    py.title(" Trajectoire navire")
    py.show()                       # Pour affichage de la figure
    
    print "Affichage: Exemple 2"
    py.figure()
    py.subplot(211)
    py.plot(data_col[1], data_col[2], 'r')
    py.xlabel("Est")
    py.ylabel("Nord")
    py.title(" Trajectoire navire")
    py.subplot(212)
    py.plot(data_col[3])    
    py.xlabel("Temps (unitaire)")
    py.ylabel("Hauteur")
    py.show()
    
    print "Affichage: Exemple 3"
    fig = plt.figure()
    ac  = fig.gca(projection="3d")
    ac.plot3D(data_col[1], data_col[2], data_col[3])
    plt.xlabel("Est")
    plt.ylabel("Nord")
    plt.title(" Trajectoire navire 3D")
    plt.show()         
    
###############################################################################    
# Le programme principale : methode main
if __name__ == "__main__":
    print "*** Test des differentes methodes ***"
    
    print " Traitement d'un fichier complexes"
    data = lectureFichierComplexe("raw_gps_short.txt") # traitement init du fichier 
    print "Taille des données: ", len(data)
    print "Exemple de données sur une ligne (dmd): ", data[0]
    print "Format de data: ", type(data)
    
    dataUTM = TraiteData(data)          # conversion des données
    print "Exemple de données sur une ligne (UTM): ", dataUTM[0]
 
    SaveData(dataUTM,"Data_UTM.txt")    # Sauvegarde dans un fichier texte

    AffichageData(dataUTM)  # Affichage des données

    print "Fin traitement"
