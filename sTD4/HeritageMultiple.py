# -*-coding:Latin-1 -*
# Test de l''heritage simple et multiple 

##############################################################################################        
# Definition de la classe A
class A(object):
    
    # constructeur de A
    def __init__(self):
        print(" Init Classe A: " + self.__class__.__name__)
        
        
    # méthode de la classe A
    def whoami(self):
        print(" Methode whoami de la classe: " + self.__class__.__name__)

##############################################################################################        
# classe B heritant de A A<-B
class B(A):
    # constructeur de B
    def __init__(self,param="rien"):
        print(" Init Classe B: " + self.__class__.__name__)
        self.parametre = param
        
##############################################################################################        
# classe C heritant de A A<-C
class C(A):
    # constructeur de C
    def __init__(self):
        A.__init__(self) 
        # ou encore 
        #super(C,self).__init__()
        
    # surcharge de la méthode whoami
    def whoami(self):
        print(" Nouvelle méthode whoami de la classe: " + self.__class__.__name__)
   
##############################################################################################        
# classe D heritant de A A<-D
class D(A):
    # constructeur de D
    def __init__(self):
        print(" New Init Classe : " + self.__class__.__name__)
        #A.__init__(self)
        # ou encore 
        super(D,self).__init__() 

##############################################################################################        
# classe E heritant de B et C (heritage multiple) (B,C)<-E    
class E(B,C): # inverser E(C,B)
    
    # si pas de constructeur pour E alors il prend le premier constructeur cité dans E(.,.) 
    #def __init__(self):
    #    print("constructeur E")
            
    # methode hello
    def hello(self):
        print("hello")
        
##############################################################################################        
# methode main (test unitaire,...)
if __name__ == "__main__":
    print('Test des classes')
    objetA = A()
    objetA.whoami()
    
    objetB = B("Mon parametre")
    objetB.whoami()
    print("Parametre: " + objetB.parametre)
    
    objetC = C()
    objetC.whoami()
    
    objetD = D()
    objetD.whoami()
    
    objetE = E()
    objetE.hello()
    
    print('Fin test')
