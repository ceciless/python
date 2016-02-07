# -*-coding:Latin-1 -*
import os
# Etude de cas : la Modélisation d'une personne.
#     Une personne peut se caractériser par : son nom, son prénom, son age, son lieu de résidence
#     Les 4 caractéristiques sont en fait les ATTRIBUTS (variables internes) qui vont représenter 
#     notre objet PERSONNE
#     On définira un compteur permettant de connaitre le nombre de personne créé. 
#     Il sera considéré comme un attribut de classe. 

# Définition de notre classe Personne
class Personne(object): 
    """ Classe définissant une personne caractérisée par :
        - nom
        - prénom
        - age
        - lieu de résidence
    """
    # Définition d'un attribut de la classe : ici un compteur de création du nombre de Personne
    objet_crees = 0 # le compteur vaut zero au départ 
    
    # constructeur de notre objet :   méthode permettant la création des attributs 
    #                                 lors de la création de l'objet
    # ICI un constructeur de base (toujours même infos pour notre objet !)
#    def __init__(self):
#        """ nos attributs """
#        self.nom    = "Dupont" # instanciation de l'attribut nom
#        self.prenom = "jean"
#        self.age    = 33
#        self.lieu   = "Brest"   
    
    # ICI un contructeur élaboré (!!! il ne peut y avoir qu'un seul et unique constructeur en python)
    # ici une astuce pour avoir simultannément 
    #    un constructeur sans parametre, equivalent au constructeur ci-dessus
    #    un constructeur avec paramettre(nom, prénom,age)
    #    le mot clef 'self' est obligatoire. c'est l'équivalent du this en Java
    def __init__(self,name="Dupont",prenom="james",old=33,ville="Brest"):
        """ nos attributs pour l'objet """
        self.nom    = name
        self.prenom = prenom
        self.age    = old
        self.lieu   = ville
        # à chaque fois que l'on créée un objet, on incrémente le compteur dans le constructeur      
        Personne.objet_crees = Personne.objet_crees + 1
        
###############################################################################################    
    # Methode permettant d'afficher proprement les attributs de l'objet
    def affichage(self):
        """Cette méthode se charge d'afficher les infos de notre objet"""
        print 'Nom/Prénom (age,lieu): ', self.nom, '/', self.prenom, '(',self.age,',',self.lieu,')'
        
    # ou encore :    
    # methode d'affichage de l'objet Personne par surcharge de __str__(self) 
    # permet d'obtenir un affichage correcte des attributs de l'objet lorsque l'on utilise print()
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{0} {1}, âgé de {2} ans à {3}".format(self.prenom, self.nom, self.age, self.lieu)
    
    # ou encore :pour un affichage correct sous l'interperteur, surchage de __repr__(self)
    def __repr__(self):
        """Quand on entre notre objet directement dans  l'interpréteur"""
        return "Personne: nom({0}), prénom({1}), âge({2}), lieu({3})".format(self.nom, self.prenom, self.age,self.lieu)
        
    def effacer(self):
        """ Cette méthode met à zeros l'objet ! pas de destruction de l'objet """
        self.nom    = ""
        self.prenom = ""
        self.age    = ""
        self.lieu   = ""     
    
    def compteur(self):
        """ Cette méthode permet d'afficher le nombre d\objet qui ont été créés"""
        print(" Nombre d\'objet: {}".format(Personne.objet_crees))
     
############################################################################################## 
# Definition d'une autre classe qui herite de la précedente : l'AgentSpecial : Personne + matricule
class AgentSpecial(Personne):
    """ Classe définissant un Agent Special heritant de Personne """
    
    # constructeur
    def __init__(self,name,matricule=0):
            #Personne.__init__(self, name) # il faut appeler explicitement le constructeur de la classe heritée !
            # ou encore :
            super(AgentSpecial,self).__init__(name)
            self.matricule = matricule


    # methode d'affichage de agenSpecial surcharge de __str__(self) pour avoir un affichage correcte des attributs de l'objet
    def __str__(self):
        return super(AgentSpecial,self).__str__() + " matricule: " + str(self.matricule) 
        #"Agent({0}), matricule({1})".format(self.nom,self.matricule)
    

##############################################################################################        
# methode main (test unitaire,...)
if __name__ == "__main__":
    print(' Test de la classe')
      
    # test1  avec un constructeur de base
    bernard = Personne()    # appel du constructeur de la classe personne / création de l'objet bernard
    bernard.affichage()
    print(bernard)
    #bernard.compteur()      # appel du compteur        
    print(bernard)
    
    print(' Détails de l\'objet 1 : ')
    print(bernard.nom)      # nom est un attribut de l'objet bernard
    print(bernard.prenom)
    print(bernard.age)
    print(bernard.lieu)
    
    print(' Modification du lieu')  # objet.attribut = nouvelle_valeur
    bernard.lieu = 'Lambe'          # ! pas nécessairement besoin des 'get' et 'set' comme en JAVA
    print(bernard.lieu)
   
    # test 2 avec un constructeur évolué
    gerard = Personne(old=20, prenom = "moimi")
    #bernard.compteur()              # appel du compteur
    print(gerard)
    print(' Détails de l\'objet 2 : ')
    print(gerard.nom)      # nom est un attribut de l'objet bernard
    print(gerard.prenom)
    print(gerard.age)
    print(gerard.lieu)

    
    print('l\'objet 3:')
    gerard2 = Personne('Micado','gerard_2',40)
    gerard2.compteur()              # appel du compteur
    print(gerard2.age)
    
    # utilisation de la méthode affichage
    print('Tests des méthodes')
    gerard2.affichage()
    print(' Affichage objet directement: ')
    print(gerard2)    # test la méthode d'affichage __repr__(self) / pas d'appel explicite de la méthode
    gerard2.effacer()
    gerard2.affichage()
        
    # Creation d'un agentSpecial
    print(' Notion d\heritage simple ')
    agent1 = AgentSpecial("Bond","007") 
    print(agent1)
    print(agent1.prenom)    # A condition que dans le constructeur de AgentSpecial on appel explictement le constructeur de la classe heritée

    
    # test d'introspection et autres petites choses
    print('Introspection sur l''objet Personne')
    print(dir(bernard))     # methode dir permet d'obtenir tous les objets sur la structure de la classe
    print(bernard.__dict__) # methode __dict__ permet de retourner les attributs et l'init du constructeur
    
    print(" ")
    print('Introspection sur l''objet AgentSpecial')
    print(dir(agent1))     # Permet de verifier qu'il possede bien les caractérisitque d'une personne avec en plus un matricule
    
    print(" A propos de issubclass ")
    print issubclass(AgentSpecial, Personne) # AgentSpecial hérite de Personne
    print issubclass(AgentSpecial, object)   # toutes les classes héritent de la classe object
    print issubclass(Personne, AgentSpecial) # Personne n'hérite pas d'AgentSpecial
    
    print(" A propos de isinstance ")
    print isinstance(agent1, AgentSpecial)   # Agent est une instance d'AgentSpecial
    print isinstance(agent1, Personne)       # Agent est une instance héritée de Personne
    
    # fin du programme
    os.system('pause')

