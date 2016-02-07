# -*- coding: utf-8 -*-

import os
import re

try:
    in_file=open("gpsdata.txt","r")
except IOError:
    print("Error")
    in_file=None;
            
date_float=[]
indice=0
if in_file!=None:
    for ligne in in_file:
        indice=indice+1;
                
        try:
            date_float.append([float (element) for element in ligne.split()])
        
        except:
            print"Error a la ligne", indice, "->",ligne,
            pass
print len(date_float)
print indice
print date_float[1]

os.system("pause")
os.system("cls")


print"Deuxieme code"
in_file.seek(0)
date_float_2=[]
indice_2=0
if in_file!=None:
    for ligne in in_file:
        indice_2=indice_2+1;
        
        try:
            date_float_2.append([float (element) for element in ligne.split()])      
        except:
            print"Error a la ligne", indice_2, "->",ligne,
            pass

print len(date_float_2)
print indice_2
print date_float[1]
        
os.system("pause")
os.system("cls")

print" Troisime "


print" Terrible "
print"Sauvegarde dans un fichier"
out_name="Date_float.txt"
out_file= open(out_name,"w")
for ligne in data_float:
    out_file.write(str(ligne))
out_file.close()

print" jolie "
out_name="Date_float_good.txt"
out_file= open(out_name,"w")
for ligne in data_float:
    for data in ligne:
        out_file.write(str(data)+" ")
    out_file.write("\n")
out_file.close()

print "possible"

    