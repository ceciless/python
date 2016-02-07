# -*-coding:Latin-1 -*
# etude multiplication et addition de liste point à point
class ListMul(list):
    
    # constructeur
    def __init__(self,Maliste):
        super(ListMul,self).__init__(Maliste)
        
        #ou encore
        #list.__init__(self,Maliste)
        
        # ou encore
        #self.extend(Maliste) # li.extend(["two", "elements"])  concatène les éléments d'une liste.
        
        #ou encore
        #for k in Maliste:
        #    self.append(k)
    
    # methode multiplication point à point
    # ici surcharge de l'opérateur de multiplication __mul__(self,other):
    # version 1 : approche classique
    """def __mul__(self,other):
        result = []
        for k in range(len(self)):
            val1 = self[k]
            val2 = other[k]
            #print val1, val2
            result.append(val1*val2)
        return result
    """
    #version 2 : une version un peu plus condensée
    def __mul__(self,other):        
        return [self[k]*other[k] for k in range(len(self))]
         
    # version 3 : version condensée avec lambda et map
    #def __mul__(self,other):
    #    return map(lambda x,y:x*y, self,other)  
    
    # surcharge de l'addition
    def __add__(self, other):
        return [self[k]+other[k] for k in range(len(self))]
    
    # surcharge de la soustraction
    def __sub__(self, other):
        return [self[k]-other[k] for k in range(len(self))]
    
##############################################################################################        
# methode main (test unitaire,...)
if __name__ == "__main__":
    
    print("Test multiplication de liste")
    
    listeA = ListMul([1,2,3,4,5])
    listeB = ListMul([6,7,8,9,0])
    listeC = ListMul([-10,11,-12,13,-14])
    
    print("Les listes: ")
    print listeA
    print listeB
    print listeC
    
    print("Multiplication: ")
    print listeA*listeB # ici on utilise la surcharge de la multiplication! on RE-défini la méthode de multiplication de python
    
    #print listeC*listeA*listeB     # probleme !
    #print (listeC*listeA)*listeB   # probleme ! 
    print listeC*(listeA*listeB)    # OK !
    
    print("Addition: ")
    print listeA+listeB
    #print listeC+listeA+listeB      # probleme ! concatenation de liste
    #print (listeC+listeA)+listeB    # probleme ! concatenation de liste
    print listeC+(listeA+listeB)     # OK !
       
    print("Soustraction: ")
    print listeA-listeB
    #print listeC-listeA-listeB      # probleme ! 
    #print (listeC-listeA)-listeB    # probleme ! 
    print listeC-(listeA+listeB)    # OK !

