# -*- coding: utf-8 -*-

print("version classique")
cr="e"
ch = "Monty python flying circus" # Chaîne fournie au départ cr = "e"  # Caractère à rechercher : # Recherche proprement dite :
lc = len(ch) # nombre de caractères à tester i = 0   # indice du caractère en cours d'examen
t = 0  # "drapeau" à 1 si le caractère recherché est présent
while i < lc:
   if ch[i] == cr:
      t = 1
   i = i + 1 # Affichage :
print "Le caractère", cr,

if t == 1:
 print "est présent",
else:
 print "est inrouvable",
 print "dans la chaîne", ch
 
 
print("version python")
ch="zorglub"
cr="e"
print cr+" est present" if cr in ch else cr+" est introuvable"