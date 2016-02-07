# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 13:43:45 2014

@author: lian
"""
import os

class Personne(object):
    objet_crees = 0
    
    def __init__(self):
        self.nom = "sssss"
        self.prenom = "ddddd"
        self.age = 22
        self.lieu = "Brest"
    
    def __init__(self,name="sssss",prenom="ddddd",age=0,ville="Brest"):
        self.nom = name
        self.prenom = prenom
        self.age = age
        self.lieu = ville    
        
        Personne.objet_crees = Personne.objet_crees + 1
    
    def affichage(self):
        print(self.nom,self.prenom,self.age,self.lieu)
    def __str__(self):
        return "{0}{1}, âgé de {2} ans à {3}",format(self.nom,self.prenom,self.age,self.lieu)
#    def __repr__(self):
#        return 
    def effacer(self):
        self.nom = ''
        self.prenom = ''
        self.age = ''
        self.lieu = ''
    def compteur(self):
        print("nombre de objet",format(Personne.objet_crees))
        
class AgentSpecial(Personne):
    def __init__(self,name,matricule=0):
        super(AgentSpecial,self).__init__(name)
        self.matricule = matricule
#    def __str__(self):
#        return "",format()
     
if __name__ == "__main__":
     print(' Test de la classe')  
     bernard = Personne()
     bernard.affichage()
     #print(bernard)
     #os.system('pause')
     
     print(bernard.nom)
     print(bernard.prenom)
     print(bernard.age)
     print(bernard.lieu)
     
     print("changer adresse")
     bernard.lieu = 'Annecy'
     print(bernard.lieu)
     
     gerard = Personne(age=20)
     #print(gerard)
     
     print(gerard.nom)
     print(gerard.prenom)
     print(gerard.age)
     print(gerard.lieu)
    
#     agent1