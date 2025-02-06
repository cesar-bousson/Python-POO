
#Job 2

'''
Créer la classe Livre qui prend en attributs privés un titre, un auteur et un
nombre de pages.
Créer les accesseurs et mutateurs nécessaires afin de pouvoir modifier et
afficher les attributs. Pour changer le nombre de pages, ce dernier doit être
un nombre entier positif, sinon la valeur n’est pas changée et un message
d’erreur est affiché.

'''

class Livre: 
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        
    # méthodes ------------------------------------    
    def get_titre(self):                                # affiche attribut privé
        return f"\nTitre du livre 1 : {self.__titre}\n"
    
    def set_titre(self, nouveau_titre):                 # affiche attribut privé
        self.__titre = nouveau_titre                    # à instancié
    
    ''''''''''''
    def get_auteur(self):                                # affiche attribut privé
        return f"\nTitre du livre 1 : {self.__auteur}\n"
    
    def set_auteur(self, nouvel_auteur):                 # affiche attribut privé
        self.__auteur = nouvel_auteur  # à instancié
        
    ''''''''''''
    
    def set_nombre_pages(self, nouveau_nbr_pages):      # affiche attribut privé  
         
        if not isinstance(nouveau_nbr_pages, int):
            print(f"Le nombre doit être un entier positif.Valeur actuelle: {self.__nombre_pages}")
            raise TypeError("Tapez des chiffres positif uniquement. Recommencez.")  
        
        if nouveau_nbr_pages <= 0:
            print(f"Saisie impossible. Nombre entier positif attendu. Valeur actuelle: {self.__nombre_pages} ")
            raise ValueError(f"Tapez des chiffres positif uniquement. Recommencez.")
        
        self.__nombre_pages = nouveau_nbr_pages # à instancié
    
    def get_nombre_pages(self):                          # affiche attribut privé
        return f"\nNombre de pages : {self.__nombre_pages}\n"
    
    
    ''''''''''''
    def get_infos_livre(self):
        return f"\nTitre : {self.__titre} | Auteur:  {self.__auteur} | Pages : {self.__nombre_pages}"      
        
# instances / objets ---------------------------------------------

livre1 = Livre("Ho'oponopono", "Luc Bodin", 118)
print(livre1.get_titre())


''''''''''''
try:
    nouveau_titre = input("Quel est le titre du nouveau livre ? : ")
    nouvel_auteur = input("Auteur du nouveau livre ? : ")
    nouveau_nbr_pages = input("Nombre de pages du nouveau livre ? : ")

    livre2 = Livre(nouveau_titre, nouvel_auteur, nouveau_nbr_pages)
    print(livre2.get_infos_livre())

except ValueError:
     print(f"Le nombre doit être un entier positif. Pages actuelles:")
except TypeError:
     print(f"Le nombre doit être un entier positif. Pages actuelles:")
     
print(livre2.get_nombre_pages())
    

''''''''''''

#  erreurs a debuguer