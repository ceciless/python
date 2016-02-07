# -*- coding: utf-8 -*-

# Affichage des éléments d'une liste

# Liste fournie au départ :

t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']

# Affichage :

i = 0
while i < len(t2):
    print t2[i],
    i = i + 1    
    
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
for elem in t2:
    print elem,
    
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
print reduce(lambda x,y: x+' '+y, t2)

help(reduce)
help(lambda)