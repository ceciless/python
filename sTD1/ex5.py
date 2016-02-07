# -*- coding: utf-8 -*-

print("version classique")
# Combinaison de deux listes en une seule
# Listes fournies au départ :
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
t3 = []  # Nouvelle liste à construire (vide au départ) 

# Boucle de traitement :
i = 0
while i < len(t1):
    t3.append(t2[i])
    t3.append(t1[i])
    i = i + 1 
    
# Affichage
print t3



t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
t3=[]
for x in zip(t2,t1):
   t3.extend(x)
print t3

help(zip)
