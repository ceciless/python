# -*-coding:Latin-1 -*
# Création d'un compteur d'objet
class compteur(object):
    
    # variable de classe permettant de compter les objets
    nbre_tour = 0
    # constructeur
    def __init__(self,nom = "objet"):
        print('initialisation')
        self.name_objet = nom
        compteur.nbre_tour += 1 
    
    # methode d'affichage
    def affichage(self):
        print('Information sur l\'objet:', self.name_objet)
        print('Nbre: ', compteur.nbre_tour)
    
    # méthode affichant le nombre d'objets
    def Nbre(self):  
        print('Nbre: ', format(compteur.nbre_tour))

##############################################################################################        
# methode main (test unitaire,...)
if __name__ == "__main__":
    print(' Test de la classe')  
    a1 = compteur()
    print("utilisation méthode affichage")
    a1.affichage()

    a2 = compteur("objet2")
    a2.affichage()
    a1.Nbre() 

    a3 = compteur("objet3")
    print(a1.nbre_tour)
    a2.Nbre()
    a3.Nbre()