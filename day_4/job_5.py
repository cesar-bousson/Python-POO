
#job 5

'''
Récupérer votre classe Forme crée juste au-dessus.

Créer une classe fille nommée Cercle qui hérite de la classe Forme et
possédant un attribut radius.
Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire
du cercle.
Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour
tester les différentes surcharges de la méthode aire en affichant les résultats
en console.

'''

import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

# Création des instances
rectangle = Rectangle(5, 10)
cercle = Cercle(7)

# Affichage des résultats
print("L'aire du rectangle est :", rectangle.aire())
print("L'aire du cercle est :", cercle.aire())
