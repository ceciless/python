# -*- coding: utf-8 -*-

# Inversion d'une chaîne de caractères
print("version classique")
ch = "zorglub" # Chaîne fournie au départ
lc = len(ch)  # nombre de caractères total
i = lc - 1  # le traitement commencera à partir du dernier  caractère
nch = ""  # nouvelle chaîne à construire (vide au départ)
while i >= 0:
    nch = nch + ch[i]
    i = i - 1 
print nch # Affichage


print("version python")

ch="zorglub"
hc=ch[::-1]
print hc


hc1=ch[0] 
print hc1 #renverrait le premier caractère: "z"
hc2=ch[3:6]
print hc2 #renverrait les caractères aux index 3, 4 et 5, donc "g", "l" et "u". Notez que la syntaxe [a:b] se lit [a,b[.
hc3=ch[-1]
print hc3 #le dernier caractère "b"
hc4=ch[::3] 
print hc4#tous les caractères du premier jusqu'au dernier par pas de 3
hc5=ch[3::]
print hc5 #tous les caractères de celui qui a l'indice 3 jusqu'au dernier.
hc6=ch[::-1]
print hc6 #tous les caractères en inversant la liste

