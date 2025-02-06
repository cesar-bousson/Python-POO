
#job 1 :

'''
Créer une classe Rectangle avec des attributs privés, longueur et largeur
initialisées dans le constructeur.
Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les
attributs de la classe.

Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5.
Changer la valeur de la longueur et de la largeur et vérifier que les
modifications soient bien prises en compte.

'''''''''''''''

class Rectangle: 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    #creation getters et setters (accesseurs et mutateurs, afficher et modifier ):
    
    # @property + (def longueur():...) ou:
    def get_longueur(self):
        return f"Longueur : {self.__longueur}"
    
    def get_largeur(self):
        return f"Largeur : {self.__largeur}"
    
    # infos des rectangles 1 et 2:    
    def get_infos_rect1(self):
        return f"\n Infos du rectangle primaire : Longueur : {self.__longueur} / Largeur : {self.__largeur}\n"
    
    def get_infos_rect2(self):
        return f"\n Infos du nouveau rectangle  : Longueur : {self.__longueur} / Largeur : {self.__largeur}\n"
    
    
    # ou @largeur.setter (def largeur(): ...)
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur # a instancier
         
    # ou @longueur.setter (def longueur():...)
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur # a instancier
        
''''''''''''''''''
#objet 1 :
rect1 = Rectangle(15, 10)

#resultats :
print(rect1.get_longueur())
print(rect1.get_largeur())

print(rect1.get_infos_rect1())

''''''''''''''''''
#modif par utilisateur HORS CLASSE (pour meilleure disponibilité des methodes de la classe):
nouvelle_longueur = int(input("Entrez nouvelle longueur: "))
nouvelle_largeur = int(input("Entrez nouvelle largeur: "))

''''''''''''''''''
#objet 2 :
rect2 = Rectangle(nouvelle_longueur, nouvelle_largeur) #nouvelle objet avec nouvelles valeurs

#resultat :
print(rect2.get_infos_rect2())
