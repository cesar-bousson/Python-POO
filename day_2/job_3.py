
# job 3 :

'''
Récupérer la classe Livre.

Ajouter l'attribut privé suivant :
- "disponible" et initialisé par défaut à True.

Créer une méthode nommée vérification qui vérifie si le livre est disponible,
c'est-à-dire que la valeur de son attribut disponible est égale à True. Cette
méthode doit retourner True ou False.

Ajouter une méthode "emprunter" qui rend le livre indisponible, autrement dit
la valeur de disponible devient False. Bien sûr, pour pouvoir emprunter un
livre, il faut que celui-ci soit disponible, vérifiez donc que celui-ci soit
disponible sans utiliser l’attribut disponible.

Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode
rendre qui dans un premier temps vérifie si le livre a bien été emprunté ( sans
utiliser l’attribut disponible), puis change la valeur de l’attribut disponible.

'''
class Livre: 
    
    def __init__(self, titre, auteur, nombre_pages):
        self.__disponible = True
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
         
        if not isinstance(nouveau_nbr_pages, int) and nouveau_nbr_pages > 0: 
            self.__nombre_pages = nouveau_nbr_pages # à instancié
        else:
            print(f"Saisie impossible. Valeur actuelle: {self.__nombre_pages} ")
            # raise ValueError(f"Tapez un nombre entier positif uniquement. Recommencez.")
        
        
    def get_nombre_pages(self):                          # affiche attribut privé
        return f"\nNombre de pages : {self.__nombre_pages}\n"
    
    
    ''''''''''''
    def get_infos_livre(self):
        return f"\nTitre : {self.__titre} | Auteur:  {self.__auteur} | Pages : {self.__nombre_pages}"      
    
    ''''''''''''
    def verification(self):
        self.__disponible = bool(self.__titre)
        return f"Ce livre est il disponible : {self.__disponible}"
    
    def emprunter(self):
        self._verif = bool(self.__titre)
        
        if self._verif == True:
            self._verif = False
            self.__disponible = self._verif 
            return f"Livre emprunté maintenant. Disponibilité du livre: {self._verif}\n"
        return "Livre indisponible"
    
    def rendre(self):
        if self._verif == False:
            self.__disponible = True
            return f"Livre rendu, disponibilité du livre : {self.__disponible}"
        return "Livre emprunté"    
        
                
# instances / objets ---------------------------------------------

livre1 = Livre("Ho'oponopono", "Luc Bodin", 118)
print(livre1.get_titre())
print(livre1.verification())
print(livre1.emprunter())
print(livre1.rendre())

''''''''''''
nouveau_titre = input("Quel est le titre du nouveau livre ? : ")
nouvel_auteur = input("Auteur du nouveau livre ? : ")
nouveau_nbr_pages = int(input("Nombre de pages du nouveau livre ? : "))

livre2 = Livre(nouveau_titre, nouvel_auteur, nouveau_nbr_pages)
print(livre2.get_infos_livre())

print(livre2.get_nombre_pages())


# ---------------------------------------------------------------- CORRECTION : ------------------------------------------

class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True  # Initialisé par défaut à True
    
    # Méthodes d'accès pour les attributs privés
    def get_titre(self):
        return f"Titre : {self.__titre}"
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return f"Auteur : {self.__auteur}"
    
    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def get_nombre_pages(self):
        return f"Nombre de pages : {self.__nombre_pages}"
    
    def set_nombre_pages(self, nouveau_nbr_pages):
        if isinstance(nouveau_nbr_pages, int) and nouveau_nbr_pages > 0:
            self.__nombre_pages = nouveau_nbr_pages
        else:
            raise ValueError("Le nombre de pages doit être un entier positif.")
    
    # Méthode pour vérifier la disponibilité
    def verification(self):
        return self.__disponible
    
    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            return "Le livre a été emprunté."
        else:
            return "Le livre est déjà emprunté et donc indisponible."
    
    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            return "Le livre a été rendu et est maintenant disponible."
        else:
            return "Le livre n'a pas été emprunté, donc il ne peut pas être rendu."
