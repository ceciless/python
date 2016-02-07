# -*- coding: utf-8 -*-

#import re
#import os
import math
import LatLongUTMconversion as LLUC
#import pylab as py
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d  import Axes3D

def dmd_to_dd(dmd):
    deg=int(math.floor(dmd/100))
    minute=dmd-deg*100.0
    return deg+minute/60.0


def TraiteData(data_float):
    print"->conversion des donnees en UTM"
    coords=[]
    for line_data in data_float:
        
        latitude=dmd_to_dd(line_data[1])
        longitude=dmd_to_dd(line_data[2])
        (zone,est,nord)=LLUC.LLtoUTM(23, latitude, longitude)
        coords.append([line_data[0], est, nord,line_data[3]])
    return coords
    
def LectureFichier(name):    
    try:
        in_file=open("gpsdata.txt","r")
    except IOError:
        print("Error")
        in_file=None;   
        
    data=[]
    indice=0
        #if in_file!=None:
    for ligne in in_file:
        indice=indice+1;
                
        try:
            data.append([float (element) for element in ligne.split()])

        except:
            print"Error a la ligne", indice, "->",ligne,
            pass
    return data
        


def SaveData(dataUTM,name):
    out_file=open(name,"w")
    for ligne in dataUTM:
        out_file.write(str(ligne[0])+" "+str(ligne[1])+" "+" "+str(ligne[2])+" "+str(ligne[3])+"\n")
    out_file.close()
    return 1
    

"""
def TestOpenFichier(namefile):
    print"->Test si presence du fichier: ",namefile
    try:
        test_file = file(namefile,"r")
        return 1
    except IOError:
        print"pas de fichier",namefile
        os.system("exit")
        return 0


def LectureFichier(namefile):
    test_in_file=TestOpenFichier(namefile)
    expreg=re.compile("\d+\.\d+ \d+\.\d+ \d+\.\d+ \d+(\.\d+)?")
    data_float=[]
    if test_in_file !=0:
        print"--> Traitement du fichier"
        
        in_file=open(namefile,"r")
        for ligne in in_file:
            if expreg.math(ligne):
                data_float.append([float (element) for element in ligne.split()])
        else:
            print" problem a la ligne: ", ligne
        
        in_file.close()
        
    return data_float
"""

    
    
if __name__ == "__main__":
    
#    print "*** Test des differentes methodes ***"    
    data=LectureFichier("gpsdata.txt")
#    print "Taille des donnees: ",len(data)
#    print "Exemple de donnees sur une ligne (dmd): ",data[0]
#    print "Format de data: ", typw(data)
    
    dataUTM = TraiteData(data)
#    print "Exemplede donnees sur une ligne (UTM): ", dataUTM[0]
    SaveData(dataUTM,"Data_UTM.txt")




