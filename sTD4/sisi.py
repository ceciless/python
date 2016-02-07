# -*- coding: utf-8 -*-

import os

class Personne(object):
    objet_cress = 0
    
    def __init__(self):
        self.nom = "sssss"
        self.prenom = "ddddd"
        self.age = 22
        self.lieu = "Brest"
        
    def __init__(self, name = "sssss", prenom="ddddd", age=0, lieu = "Brest"):
        self.nom = name
        self.prenom = prenom
        self.age = age
        self.lieu = ville
        
        Personne.objet_cress = Personne.objet_cress + 1
        
    def affichage(self):
        print(self.nom,self.prenom, self.age, self.lieu)
        
    def __str__ (self):
        return"{0}{1}, age de {2} ans a {3}", format(self.nom, self.prenom, self.age, self.lieu)
        
    def __repr__(self):
        return
        
    def effacer(self):
        self.nom='' 
        self.prenom='' 
        self.age='' 
        self.lieu=''
        
    def compteur(self):
        print("nombre de objets",format(Personne.objet_cress))
        
if __name__ == "__main__":
    print(' Test de la classe')   
    bernard = Personne()
    bernard.affichage()
    print(bernard)
    os.system('pause')
    
    print(bernnard.nom)
    print(bernnard.prenom)
    print(bernnard.age)
    print(bernnard.lieu)
    
    print("changer adresse")
    bernard.lieu = 'Annecy'
    print(bernard.lieu)
    
    gerard = Personne (age=20)
    print(gernard)
    
    
    
    
    
    
        

