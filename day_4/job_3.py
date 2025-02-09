

#Job 3
'''
Créer une classe Rectangle avec comme attribut privé longueur et largeur.
Créer la méthode perimètre permettant de calculer le périmètre du
rectangle ainsi que la méthode surface permettant de calculer la surface du
rectangle.

Créer les assesseurs et mutateurs permettant de manipuler les attributs de
la classe.

Créer une classe Parallelepipede héritant de la classe Rectangle avec en
plus un attribut hauteur et une autre méthode volume, permettant de
calculer le volume du parallélépipède.

Instancier la classe Rectangle et assurez-vous que toutes les méthodes
fonctionnent.

'''

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur

    def __str__(self):
        return f"Rectangle(longueur={self.__longueur}, largeur={self.__largeur})"


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Assesseur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour la hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume
    def volume(self):
        return self.surface() * self.__hauteur

    def __str__(self):
        return (f"Parallelepipede(longueur={self.get_longueur()}, largeur={self.get_largeur()}, "
                f"hauteur={self.__hauteur})")


# Instanciation et tests de la classe Rectangle
rectangle = Rectangle(5, 3)
print(rectangle)
print(f"Périmètre: {rectangle.perimetre()}")
print(f"Surface: {rectangle.surface()}")

# Modification des dimensions
rectangle.set_longueur(10)
rectangle.set_largeur(4)
print(rectangle)
print(f"Périmètre après modification: {rectangle.perimetre()}")
print(f"Surface après modification: {rectangle.surface()}")

# Instanciation et tests de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 3, 2)
print(parallelepipede)
print(f"Volume: {parallelepipede.volume()}")

# Modification des dimensions
parallelepipede.set_longueur(8)
parallelepipede.set_largeur(6)
parallelepipede.set_hauteur(4)
print(parallelepipede)
print(f"Volume après modification: {parallelepipede.volume()}")
